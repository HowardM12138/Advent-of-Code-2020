def part1(tile_dict):
    match = {}
    for tile_id, tile in tile_dict.items():
        edges = [tile[0], tile[-1], "".join([l[0] for l in tile]), "".join([l[-1] for l in tile])]
        matched_tiles = find(tile_dict, edges, tile_id)
        match[tile_id] = matched_tiles
    return match


def find(tile_dict, edges, current_id):
    matched_tiles = []
    for tile_id, tile in tile_dict.items():
        if tile_id != current_id and match(tile, edges):
            matched_tiles.append(tile_id)
    return matched_tiles

def match(tile, edges_to_match):
    edges = [tile[0], tile[-1], "".join([l[0] for l in tile]), "".join([l[-1] for l in tile])]
    for edge in edges:
        edge_inverse = "".join([edge[len(edge) - i - 1] for i in range(len(edge))])
        if edge in edges_to_match or edge_inverse in edges_to_match:
            return True
    return False






lines = open("./input.txt", "r").readlines()

tile_dict = {}
tile_id = 0
for line in lines:
    line = line.strip()
    if "Tile" in line:
        tile_id = int(line.split(" ")[1][:-1])
        tile_dict[tile_id] = []
    elif line != "":
        tile_dict[tile_id].append(line)

match = part1(tile_dict)
def get(id):
    return match[id]