from feed.models.snail import Snail


def json_to_snail(snail_json):
    snail = Snail(snail_json['id'], snail_json['name'], snail_json['trainer']['id'])
    return snail
