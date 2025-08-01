import numpy as np

def distance(lat1, lon1, lat2, lon2):
    # Approximate radius of earth in km
    R = 6373.0

    lat1 = lat1 * np.pi / 180.0
    lon1 = np.deg2rad(lon1)
    lat2 = np.deg2rad(lat2)
    lon2 = np.deg2rad(lon2)

    d = np.sin((lat2 - lat1)/2) **2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1)/2) **2

    return 2 * R * np.arcsin(np.sqrt(d))

def velocity(v0, v1):
    # Get boat speed
    BS = np.sqrt(v0[0] **2 + v0[1] **2)

    # Get true wind speed
    TWS = np.sqrt(v1[0] **2 + v1[1] **2)

    # Get true wind angle
    #TWA = np.arctan2(np.linalg.det([v1, v0]), np.dot(v1, v0)) + np.pi
    TWA = np.arctan2(*v1.T[::-1])

    # Get apparent wind speed
    AWS = np.sqrt(TWS **2 + BS **2 + 2 * TWS * BS * np.cos(TWA))

    # Get apparent wind angle
    AWA = np.arccos( (TWS * np.cos(TWA) + BS) / AWS)
    v2 = np.cross([*v0, 0.], [*v1, 0.])
    if v2[2] > 0:
        AWA = 2 * np.pi - AWA

    return TWS, TWA, AWS, AWA
