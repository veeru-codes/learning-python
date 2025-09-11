playlist = {
    'title': 'patagonia bus',
    'author': 'colt steele',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.2},
        {'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
        {'title': 'song2', 'artist': ['garfield'], 'duration': 2.0},
    ]
}

total_duration = 0
for song in playlist['songs']:
    total_duration += song['duration']

print(f"total duration: {total_duration}")
