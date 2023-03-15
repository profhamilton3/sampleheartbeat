def on_forever():
    basic.show_icon(IconNames.HEART, 1000)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_icon(IconNames.SMALL_HEART, 600)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
basic.forever(on_forever)
