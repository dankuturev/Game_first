from game.scenes import StartRoom, Death, Finished, SecondRoom, ThirdRoom, FourthRoom


class Map(object):
    scenes = {
        'start_room': StartRoom(),
        'second_room': SecondRoom(),
        'third_room': ThirdRoom(),
        'fourth_room': FourthRoom(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene  # 'central_corridor

    @staticmethod
    def next_scene(scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('start_room')
