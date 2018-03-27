from django.db import models


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
        return str(self.team_number) + " - " + str(self.match_number)

