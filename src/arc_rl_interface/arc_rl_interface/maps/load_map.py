import yaml

def load_map(yaml_path):
    with open(yaml_path, 'r') as f:
        map_data = yaml.safe_load(f)
    return map_data
