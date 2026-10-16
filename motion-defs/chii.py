"""Motion definitions for Chii (chii).

Composite Action-group motions built from the parameter usage learned from
the model's 20 bundled motions (see tools/analyze_model.py):

- smile = EyeLSmile/EyeRSmile=1 + MouthForm=1 (no EyeOpen=0 needed here,
  unlike Hiyori)
- angry brows = BrowLY/RY=-1 + BrowLForm/RForm=+1
- sad brows   = BrowLY/RY=+0.5 + BrowLForm/RForm=-1
- shy         = Cheek=1 + gaze down/side (EyeBallY=-0.4, EyeBallX=0.3)
  + MouthForm=0.35
- base pose is all zeros except EyeOpen=1 (MouthForm rests at 0)
- ranges observed: head angles +-30, body angles +-10, everything else
  within the analyze output; blink is baked into EyeOpen where a motion
  runs long (auto-blink pauses while a motion plays)
"""


def define(curve, motion):
    MOTIONS = {}

    # ---------------------------------------------------------------- happy
    D = 2.8
    MOTIONS["chii_happy"] = motion(D, [
        curve("ParamEyeLSmile", [(0, 0), (0.3, 1), (2.2, 1), (D, 0)]),
        curve("ParamEyeRSmile", [(0, 0), (0.3, 1), (2.2, 1), (D, 0)]),
        curve("ParamMouthForm", [(0, 0), (0.3, 1), (2.2, 1), (D, 0)]),
        curve("ParamMouthOpenY", [(0, 0), (0.35, 0.4), (0.8, 0.15), (1.2, 0.35), (1.8, 0.1), (D, 0)]),
        curve("ParamCheek", [(0, 0), (0.4, 0.8), (2.2, 0.8), (D, 0)]),
        curve("ParamBrowLY", [(0, 0), (0.3, 0.4), (2.2, 0.4), (D, 0)]),
        curve("ParamBrowRY", [(0, 0), (0.3, 0.4), (2.2, 0.4), (D, 0)]),
        # cheerful head wobble, one baked blink in the middle
        curve("ParamAngleZ", [(0, 0), (0.5, 8), (1.2, -8), (1.9, 5), (D, 0)]),
        curve("ParamAngleY", [(0, 0), (0.4, -4), (1.0, 4), (1.6, -3), (D, 0)]),
        curve("ParamBodyAngleZ", [(0, 0), (0.5, -4), (1.2, 4), (1.9, -2), (D, 0)]),
        curve("ParamEyeLOpen", [(0, 1), (1.25, 1), (1.35, 0), (1.5, 1), (D, 1)]),
        curve("ParamEyeROpen", [(0, 1), (1.25, 1), (1.35, 0), (1.5, 1), (D, 1)]),
    ])

    # ---------------------------------------------------------------- nod
    D = 2.0
    MOTIONS["chii_nod"] = motion(D, [
        curve("ParamAngleY", [(0, 0), (0.35, -18), (0.65, 3), (1.0, -14), (1.5, 0), (D, 0)]),
        curve("ParamBodyAngleY", [(0, 0), (0.4, -3), (1.05, -2), (1.6, 0), (D, 0)]),
        curve("ParamEyeLSmile", [(0, 0), (0.35, 0.7), (1.4, 0.7), (D, 0)]),
        curve("ParamEyeRSmile", [(0, 0), (0.35, 0.7), (1.4, 0.7), (D, 0)]),
        curve("ParamMouthForm", [(0, 0), (0.35, 1), (1.4, 1), (D, 0)]),
        curve("ParamEyeLOpen", [(0, 1), (0.35, 0.6), (0.65, 0.9), (1.0, 0.65), (1.5, 1), (D, 1)]),
        curve("ParamEyeROpen", [(0, 1), (0.35, 0.6), (0.65, 0.9), (1.0, 0.65), (1.5, 1), (D, 1)]),
    ])

    # --------------------------------------------------------- head shake
    D = 2.4
    MOTIONS["chii_shakehead"] = motion(D, [
        # the bundled head_shake group reaches +-24, stay within that
        curve("ParamAngleX", [(0, 0), (0.35, -22), (0.8, 18), (1.25, -14), (1.7, 8), (2.1, 0), (D, 0)]),
        curve("ParamBodyAngleX", [(0, 0), (0.4, -3), (0.85, 2), (1.3, -1), (1.8, 0), (D, 0)]),
        curve("ParamEyeLOpen", [(0, 1), (0.35, 0.7), (1.7, 0.7), (2.1, 1), (D, 1)]),
        curve("ParamEyeROpen", [(0, 1), (0.35, 0.7), (1.7, 0.7), (2.1, 1), (D, 1)]),
        # mild refusal: slightly lowered brows + a small pout
        curve("ParamBrowLY", [(0, 0), (0.35, -0.3), (1.7, -0.3), (2.1, 0), (D, 0)]),
        curve("ParamBrowRY", [(0, 0), (0.35, -0.3), (1.7, -0.3), (2.1, 0), (D, 0)]),
        curve("ParamBrowLForm", [(0, 0), (0.35, 0.4), (1.7, 0.4), (2.1, 0), (D, 0)]),
        curve("ParamBrowRForm", [(0, 0), (0.35, 0.4), (1.7, 0.4), (2.1, 0), (D, 0)]),
        curve("ParamMouthForm", [(0, 0), (0.35, -0.5), (1.7, -0.5), (2.1, 0), (D, 0)]),
    ])

    # ------------------------------------------------------------- curious
    D = 3.2
    MOTIONS["chii_curious"] = motion(D, [
        # head tilts and the gaze follows, like inspecting something
        curve("ParamAngleZ", [(0, 0), (0.7, 14), (2.4, 14), (D, 0)]),
        curve("ParamAngleX", [(0, 0), (0.8, 8), (2.4, 8), (D, 0)]),
        curve("ParamAngleY", [(0, 0), (0.8, 4), (2.4, 4), (D, 0)]),
        curve("ParamEyeBallX", [(0, 0), (0.7, -0.7), (2.4, -0.7), (D, 0)]),
        curve("ParamEyeBallY", [(0, 0), (0.7, 0.4), (2.4, 0.4), (D, 0)]),
        curve("ParamMouthOpenY", [(0, 0), (0.7, 0.2), (2.4, 0.2), (D, 0)]),
        curve("ParamMouthForm", [(0, 0), (0.7, 0.2), (2.4, 0.2), (D, 0)]),
        curve("ParamBrowLY", [(0, 0), (0.7, 0.3), (2.4, 0.3), (D, 0)]),
        curve("ParamBrowRY", [(0, 0), (0.7, 0.3), (2.4, 0.3), (D, 0)]),
        curve("ParamBodyAngleZ", [(0, 0), (0.8, 5), (2.4, 5), (D, 0)]),
        curve("ParamEyeLOpen", [(0, 1), (1.4, 1), (1.5, 0), (1.65, 1), (D, 1)]),
        curve("ParamEyeROpen", [(0, 1), (1.4, 1), (1.5, 0), (1.65, 1), (D, 1)]),
    ])

    # ----------------------------------------------------------------- shy
    D = 3.6
    MOTIONS["chii_shy"] = motion(D, [
        curve("ParamCheek", [(0, 0), (0.6, 1), (2.8, 1), (D, 0)]),
        curve("ParamEyeBallY", [(0, 0), (0.6, -0.4), (2.8, -0.4), (D, 0)]),
        curve("ParamEyeBallX", [(0, 0), (0.6, 0.3), (2.8, 0.3), (D, 0)]),
        curve("ParamEyeLOpen", [(0, 1), (0.6, 0.65), (2.8, 0.65), (D, 1)]),
        curve("ParamEyeROpen", [(0, 1), (0.6, 0.65), (2.8, 0.65), (D, 1)]),
        curve("ParamMouthForm", [(0, 0), (0.6, 0.35), (2.8, 0.35), (D, 0)]),
        curve("ParamAngleY", [(0, 0), (0.7, -10), (2.8, -10), (D, 0)]),
        curve("ParamAngleZ", [(0, 0), (0.9, 5), (1.8, 3), (2.8, 5), (D, 0)]),
        curve("ParamBodyAngleZ", [(0, 0), (1.0, 3), (2.0, -2), (2.9, 3), (D, 0)]),
    ])

    # -------------------------------------- talking smile (loop, while speaking)
    # Held while the character speaks: happy expression + gentle bobbing.
    # ParamMouthOpenY (LipSync group) is deliberately left out so the
    # player's lip sync owns it; blinks are baked into EyeOpen.
    D = 3.0
    MOTIONS["chii_talk_smile"] = motion(D, [
        # oscillating curves use periods of D/n so they meet at the seam,
        # and the seam sits mid-swing, never at an extreme
        curve("ParamAngleY", [(0, 2), (0.75, 5), (1.5, 2), (2.25, -1), (D, 2)], loop=True),
        curve("ParamAngleZ", [(0, -3), (0.75, 0), (1.5, 3), (2.25, 0), (D, -3)], loop=True),
        curve("ParamBodyAngleX", [(0, 0), (0.75, 2), (1.5, 0), (2.25, -2), (D, 0)], loop=True),
        curve("ParamBodyAngleZ", [(0, 1), (1.5, -1), (D, 1)], loop=True),
        curve("ParamEyeLSmile", [(0, 1), (D, 1)], loop=True),
        curve("ParamEyeRSmile", [(0, 1), (D, 1)], loop=True),
        curve("ParamMouthForm", [(0, 1), (D, 1)], loop=True),
        curve("ParamCheek", [(0, 0.4), (D, 0.4)], loop=True),
        curve("ParamBrowLY", [(0, 0.3), (D, 0.3)], loop=True),
        curve("ParamBrowRY", [(0, 0.3), (D, 0.3)], loop=True),
        # one blink per cycle, baked in; the seam itself stays flat at 1
        curve("ParamEyeLOpen", [(0, 1), (2.35, 1), (2.45, 0), (2.6, 1), (D, 1)], loop=True),
        curve("ParamEyeROpen", [(0, 1), (2.35, 1), (2.45, 0), (2.6, 1), (D, 1)], loop=True),
    ], loop=True)

    # Entries registered into the "Action" group of model3.json
    # (display name shown in the WebUI, fade-in/out seconds)
    MANIFEST = [
        ("chii_happy", "开心", 0.4, 0.5),
        ("chii_nod", "点头", 0.3, 0.5),
        ("chii_shakehead", "摇头", 0.3, 0.5),
        ("chii_curious", "好奇", 0.5, 0.5),
        ("chii_shy", "害羞", 0.5, 0.5),
        ("chii_talk_smile", "说话微笑(循环)", 0.4, 0.5),
    ]
    return MOTIONS, MANIFEST
