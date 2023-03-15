basic.forever(function on_forever() {
    basic.showIcon(IconNames.Heart, 1000)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
    basic.showIcon(IconNames.SmallHeart, 600)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
})
