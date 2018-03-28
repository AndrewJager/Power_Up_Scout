from django.db import models


class Robot(models.Model):
    team_number = models.IntegerField(default=0)


class Survey(models.Model):
    auto_choices = (
        ('None', 'None'),
        ('Baseline', 'Baseline'),
        ('CenterSwitch', 'Center Switch'),
        ('SideSwitch', 'Side Switch'),
        ('Scale', 'Scale')
    )

    #
    # team number - number
    team_number = models.IntegerField(default=0)

    robot = models.ForeignKey(Robot, on_delete=models.CASCADE, null=True)

    match_number = models.CharField(max_length=200)

    # Auton - selectable list(None, Baseline, Center switch, side switch, scale)
    auton = models.CharField(
        max_length=30,
        choices=auto_choices,
        default='None',
    )

    # auto cubes - number
    auto_cubes = models.IntegerField(default=0)

    # auto notes - string
    auto_notes = models.CharField(max_length=200, blank=True, null=True)

    # cubes in own switch - number
    own_switch_cubes = models.IntegerField(default=0)

    # cubes in opponents switch - number
    other_switch_cubes = models.IntegerField(default=0)

    # cubes in scale - number
    scale_cubes = models.IntegerField(default=0)

    # cubes in vault - number
    vault_cubes = models.IntegerField(default=0)

    # teleoperated notes - string
    tele_notes = models.CharField(max_length=200, blank=True, null=True)

    # Climbs - bool
    can_climb = models.BooleanField(default=False)

    # climbs with others - bool
    buddy_climb = models.BooleanField(default=False)

    # speed of robot - number (1-10)
    robot_speed = models.IntegerField(default=0)

    # Proficiency at Picking up Cubes - number (1-10)
    robot_cube_intake = models.IntegerField(default=0)

    # Proficiency at Keeping Hold of Cubes - number (1-10)
    robot_cube_holding = models.IntegerField(default=0)

    # Proficiency at Placing Cubes - number (1-10)
    robot_cube_placing = models.IntegerField(default=0)

    # additional notes - string
    other_notes = models.CharField(max_length=200, blank=True, null=True)

    # name of person who submitted report
    scouter_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.team_number) + " - match " + str(self.match_number)

    @classmethod
    def stringToObject(cls, string):
        string = '[{"name":"team_number","value":"333"},' \
                 + '{"name":"match_number","value":"010"}]' \
                 + '{"name":"auton","value":"?????????????????????????????????????????????"}]' \
                 + '{"name":"auton_cubes","value":"455"}]' \
                 + '{"name":"auton_notes","value":"auto notes"}]' \
                 + '{"name":"own_switch_cubes","value":"455"}]' \
                 + '{"name":"other_switch_cubes","value":"455"}]' \
                 + '{"name":"scale_cubes","value":"455"}]' \
                 + '{"name":"vault_cubes","value":"455"}]' \
                 + '{"name":"tele_notes","value":"teleoperated notes"}]' \
                 + '{"name":"can_climb","value":"False"}]' \
                 + '{"name":"buddy_climb","value":"False"}]' \
                 + '{"name":"robot_speed","value":"455"}]' \
                 + '{"name":"robot_cube_intake","value":"455"}]' \
                 + '{"name":"robot_cube_holding","value":"455"}]' \
                 + '{"name":"robot_cube_placing","value":"455"}]' \
                 + '{"name":"other_notes","value":"other notes"}]' \
                 + '{"name":"scouter_name","value":"scouter"}]'
