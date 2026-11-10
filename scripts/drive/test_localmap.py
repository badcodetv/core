"""Path translation between machines: python3 -m pytest scripts/drive/test_localmap.py (or run it directly)."""
import json, pathlib, sys, tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import localmap  # noqa: E402

JACK = r'C:\Users\jackt\OneDrive\Desktop\Youtube Vids\Karen music vid'
FOLDERS = {'folders': {
    'karen-music': {'drive': 'x', 'drive_name': 'Karen Music ',
                    'homes': ['/mnt/d/badcode-videos/karen-music',
                              '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/Karen music vid']},
    'karen-story': {'drive': 'y', 'drive_name': 'Karen Story', 'homes': ['/mnt/d/badcode-videos/karen-story']},
}}


def machine(stories):
    d = pathlib.Path(tempfile.mkdtemp())
    (d / 'local.json').write_text(json.dumps({'stories': stories}))
    (d / 'folders.json').write_text(json.dumps(FOLDERS))
    localmap.LOCAL, localmap.FOLDERS, localmap._HOMES = d / 'local.json', d / 'folders.json', None
    localmap._env = lambda: 'wsl'


def test_kai_paths_open_on_jacks_machine():
    machine({'karen-music': JACK})
    assert localmap.localize_path('/mnt/d/badcode-videos/karen-music/clips/a.mp4') == \
        '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/Karen music vid/clips/a.mp4'
    assert localmap.localize_path(r'D:\badcode-videos\karen-music\clips\a.mp4') == JACK + r'\clips\a.mp4'


def test_jacks_paths_open_on_kais_machine():
    machine({'karen-music': r'D:\badcode-videos\karen-music'})
    assert localmap.localize_path('/mnt/c/Users/jackt/OneDrive/Desktop/YouTube vids/Karen music vid/v/b.mp4') == \
        '/mnt/d/badcode-videos/karen-music/v/b.mp4'  # case differs: Windows drives ignore case
    assert localmap.localize_path('/mnt/d/badcode-videos/karen-music/clips/a.mp4') == \
        '/mnt/d/badcode-videos/karen-music/clips/a.mp4'


def test_what_must_not_change():
    machine({'karen-music': JACK})
    same = ['/mnt/d/badcode-videos/karen-music-old/x.mp4',      # a different folder sharing a prefix
            '/mnt/d/badcode-videos/karen-story/x.mp4',          # a story this machine hasn't mapped
            'https://claude.ai/artifact/abc', 'hello', '', 3, None, '/']
    for v in same:
        assert localmap.localize_path(v) == v
    doc = {'src': '/mnt/d/badcode-videos/karen-music/a.mp4', 'n': 2, 'list': ['/mnt/d/badcode-videos/karen-music']}
    out = localmap.localize(doc)
    assert out['n'] == 2 and out['list'] == ['/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/Karen music vid']
    assert out['src'].endswith('Karen music vid/a.mp4')


if __name__ == '__main__':
    for name, f in list(globals().items()):
        if name.startswith('test_'):
            f(); print('ok', name)
