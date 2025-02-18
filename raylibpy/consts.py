from enum import IntEnum, IntFlag, auto

__all__ = [
    'ConfigFlags',
    'FLAG_VSYNC_HINT',
    'FLAG_FULLSCREEN_MODE',
    'FLAG_WINDOW_RESIZABLE',
    'FLAG_WINDOW_UNDECORATED',
    'FLAG_WINDOW_HIDDEN',
    'FLAG_WINDOW_MINIMIZED',
    'FLAG_WINDOW_MAXIMIZED',
    'FLAG_WINDOW_UNFOCUSED',
    'FLAG_WINDOW_TOPMOST',
    'FLAG_WINDOW_ALWAYS_RUN',
    'FLAG_WINDOW_TRANSPARENT',
    'FLAG_WINDOW_HIGHDPI',
    'FLAG_MSAA_4X_HINT',
    'FLAG_INTERLACED_HINT',

    'TraceLogLevel',
    'LOG_ALL',
    'LOG_TRACE',
    'LOG_DEBUG',
    'LOG_INFO',
    'LOG_WARNING',
    'LOG_ERROR',
    'LOG_FATAL',
    'LOG_NONE',

    'KeyboardKey',
    'KEY_NULL',
    'KEY_APOSTROPHE',
    'KEY_COMMA',
    'KEY_MINUS',
    'KEY_PERIOD',
    'KEY_SLASH',
    'KEY_ZERO',
    'KEY_ONE',
    'KEY_TWO',
    'KEY_THREE',
    'KEY_FOUR',
    'KEY_FIVE',
    'KEY_SIX',
    'KEY_SEVEN',
    'KEY_EIGHT',
    'KEY_NINE',
    'KEY_SEMICOLON',
    'KEY_EQUAL',
    'KEY_A',
    'KEY_B',
    'KEY_C',
    'KEY_D',
    'KEY_E',
    'KEY_F',
    'KEY_G',
    'KEY_H',
    'KEY_I',
    'KEY_J',
    'KEY_K',
    'KEY_L',
    'KEY_M',
    'KEY_N',
    'KEY_O',
    'KEY_P',
    'KEY_Q',
    'KEY_R',
    'KEY_S',
    'KEY_T',
    'KEY_U',
    'KEY_V',
    'KEY_W',
    'KEY_X',
    'KEY_Y',
    'KEY_Z',
    'KEY_SPACE',
    'KEY_ESCAPE',
    'KEY_ENTER',
    'KEY_TAB',
    'KEY_BACKSPACE',
    'KEY_INSERT',
    'KEY_DELETE',
    'KEY_RIGHT',
    'KEY_LEFT',
    'KEY_DOWN',
    'KEY_UP',
    'KEY_PAGE_UP',
    'KEY_PAGE_DOWN',
    'KEY_HOME',
    'KEY_END',
    'KEY_CAPS_LOCK',
    'KEY_SCROLL_LOCK',
    'KEY_NUM_LOCK',
    'KEY_PRINT_SCREEN',
    'KEY_PAUSE',
    'KEY_F1',
    'KEY_F2',
    'KEY_F3',
    'KEY_F4',
    'KEY_F5',
    'KEY_F6',
    'KEY_F7',
    'KEY_F8',
    'KEY_F9',
    'KEY_F10',
    'KEY_F11',
    'KEY_F12',
    'KEY_LEFT_SHIFT',
    'KEY_LEFT_CONTROL',
    'KEY_LEFT_ALT',
    'KEY_LEFT_SUPER',
    'KEY_RIGHT_SHIFT',
    'KEY_RIGHT_CONTROL',
    'KEY_RIGHT_ALT',
    'KEY_RIGHT_SUPER',
    'KEY_KB_MENU',
    'KEY_LEFT_BRACKET',
    'KEY_BACKSLASH',
    'KEY_RIGHT_BRACKET',
    'KEY_GRAVE',
    'KEY_KP_0',
    'KEY_KP_1',
    'KEY_KP_2',
    'KEY_KP_3',
    'KEY_KP_4',
    'KEY_KP_5',
    'KEY_KP_6',
    'KEY_KP_7',
    'KEY_KP_8',
    'KEY_KP_9',
    'KEY_KP_DECIMAL',
    'KEY_KP_DIVIDE',
    'KEY_KP_MULTIPLY',
    'KEY_KP_SUBTRACT',
    'KEY_KP_ADD',
    'KEY_KP_ENTER',
    'KEY_KP_EQUAL',
    'KEY_BACK',
    'KEY_MENU',
    'KEY_VOLUME_UP',
    'KEY_VOLUME_DOWN',

    'MouseButton',
    'MOUSE_BUTTON_LEFT',
    'MOUSE_BUTTON_RIGHT',
    'MOUSE_BUTTON_MIDDLE',

    'MouseCursor',
    'MOUSE_CURSOR_DEFAULT',
    'MOUSE_CURSOR_ARROW',
    'MOUSE_CURSOR_IBEAM',
    'MOUSE_CURSOR_CROSSHAIR',
    'MOUSE_CURSOR_POINTING_HAND',
    'MOUSE_CURSOR_RESIZE_EW',
    'MOUSE_CURSOR_RESIZE_NS',
    'MOUSE_CURSOR_RESIZE_NWSE',
    'MOUSE_CURSOR_RESIZE_NESW',
    'MOUSE_CURSOR_RESIZE_ALL',
    'MOUSE_CURSOR_NOT_ALLOWED',

    'GamepadButton',
    'GAMEPAD_BUTTON_UNKNOWN',
    'GAMEPAD_BUTTON_LEFT_FACE_UP',
    'GAMEPAD_BUTTON_LEFT_FACE_RIGHT',
    'GAMEPAD_BUTTON_LEFT_FACE_DOWN',
    'GAMEPAD_BUTTON_LEFT_FACE_LEFT',
    'GAMEPAD_BUTTON_RIGHT_FACE_UP',
    'GAMEPAD_BUTTON_RIGHT_FACE_RIGHT',
    'GAMEPAD_BUTTON_RIGHT_FACE_DOWN',
    'GAMEPAD_BUTTON_RIGHT_FACE_LEFT',
    'GAMEPAD_BUTTON_LEFT_TRIGGER_1',
    'GAMEPAD_BUTTON_LEFT_TRIGGER_2',
    'GAMEPAD_BUTTON_RIGHT_TRIGGER_1',
    'GAMEPAD_BUTTON_RIGHT_TRIGGER_2',
    'GAMEPAD_BUTTON_MIDDLE_LEFT',
    'GAMEPAD_BUTTON_MIDDLE',
    'GAMEPAD_BUTTON_MIDDLE_RIGHT',
    'GAMEPAD_BUTTON_LEFT_THUMB',
    'GAMEPAD_BUTTON_RIGHT_THUMB',

    'GamepadAxis',
    'GAMEPAD_AXIS_LEFT_X',
    'GAMEPAD_AXIS_LEFT_Y',
    'GAMEPAD_AXIS_RIGHT_X',
    'GAMEPAD_AXIS_RIGHT_Y',
    'GAMEPAD_AXIS_LEFT_TRIGGER',
    'GAMEPAD_AXIS_RIGHT_TRIGGER',

    'MaterialMapIndex',
    'MATERIAL_MAP_ALBEDO',
    'MATERIAL_MAP_METALNESS',
    'MATERIAL_MAP_NORMAL',
    'MATERIAL_MAP_ROUGHNESS',
    'MATERIAL_MAP_OCCLUSION',
    'MATERIAL_MAP_EMISSION',
    'MATERIAL_MAP_HEIGHT',
    'MATERIAL_MAP_BRDG',
    'MATERIAL_MAP_CUBEMAP',
    'MATERIAL_MAP_IRRADIANCE',
    'MATERIAL_MAP_PREFILTER',
    'MATERIAL_MAP_DIFFUSE',
    'MATERIAL_MAP_SPECULAR',

    'ShaderLocationIndex',
    'SHADER_LOC_VERTEX_POSITION',
    'SHADER_LOC_VERTEX_TEXCOORD01',
    'SHADER_LOC_VERTEX_TEXCOORD02',
    'SHADER_LOC_VERTEX_NORMAL',
    'SHADER_LOC_VERTEX_TANGENT',
    'SHADER_LOC_VERTEX_COLOR',
    'SHADER_LOC_MATRIX_MVP',
    'SHADER_LOC_MATRIX_VIEW',
    'SHADER_LOC_MATRIX_PROJECTION',
    'SHADER_LOC_MATRIX_MODEL',
    'SHADER_LOC_MATRIX_NORMAL',
    'SHADER_LOC_VECTOR_VIEW',
    'SHADER_LOC_COLOR_DIFFUSE',
    'SHADER_LOC_COLOR_SPECULAR',
    'SHADER_LOC_COLOR_AMBIENT',
    'SHADER_LOC_MAP_ALBEDO',
    'SHADER_LOC_MAP_METALNESS',
    'SHADER_LOC_MAP_NORMAL',
    'SHADER_LOC_MAP_ROUGHNESS',
    'SHADER_LOC_MAP_OCCLUSION',
    'SHADER_LOC_MAP_EMISSION',
    'SHADER_LOC_MAP_HEIGHT',
    'SHADER_LOC_MAP_CUBEMAP',
    'SHADER_LOC_MAP_IRRADIANCE',
    'SHADER_LOC_MAP_PREFILTER',
    'SHADER_LOC_MAP_BRDF',
    'SHADER_LOC_MAP_DIFFUSE',
    'SHADER_LOC_MAP_SPECULAR',

    'ShaderUniformDataType',
    'SHADER_UNIFORM_FLOAT',
    'SHADER_UNIFORM_VEC2',
    'SHADER_UNIFORM_VEC3',
    'SHADER_UNIFORM_VEC4',
    'SHADER_UNIFORM_INT',
    'SHADER_UNIFORM_IVEC2',
    'SHADER_UNIFORM_IVEC3',
    'SHADER_UNIFORM_IVEC4',
    'SHADER_UNIFORM_SAMPLER2D',

    'PixelFormat',
    'PIXELFORMAT_UNCOMPRESSED_GRAYSCALE',
    'PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA',
    'PIXELFORMAT_UNCOMPRESSED_R5G6B5',
    'PIXELFORMAT_UNCOMPRESSED_R8G8B8',
    'PIXELFORMAT_UNCOMPRESSED_R5G5B5A1',
    'PIXELFORMAT_UNCOMPRESSED_R4G4B4A4',
    'PIXELFORMAT_UNCOMPRESSED_R8G8B8A8',
    'PIXELFORMAT_UNCOMPRESSED_R32',
    'PIXELFORMAT_UNCOMPRESSED_R32G32B32',
    'PIXELFORMAT_UNCOMPRESSED_R32G32B32A32',
    'PIXELFORMAT_COMPRESSED_DXT1_RGB',
    'PIXELFORMAT_COMPRESSED_DXT1_RGBA',
    'PIXELFORMAT_COMPRESSED_DXT3_RGBA',
    'PIXELFORMAT_COMPRESSED_DXT5_RGBA',
    'PIXELFORMAT_COMPRESSED_ETC1_RGB',
    'PIXELFORMAT_COMPRESSED_ETC2_RGB',
    'PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA',
    'PIXELFORMAT_COMPRESSED_PVRT_RGB',
    'PIXELFORMAT_COMPRESSED_PVRT_RGBA',
    'PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA',
    'PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA',

    'TextureFilter',
    'TEXTURE_FILTER_POINT',
    'TEXTURE_FILTER_BILINEAR',
    'TEXTURE_FILTER_TRILINEAR',
    'TEXTURE_FILTER_ANISOTROPIC_4X',
    'TEXTURE_FILTER_ANISOTROPIC_8X',
    'TEXTURE_FILTER_ANISOTROPIC_16X',

    'TextureWrap',
    'TEXTURE_WRAP_REPEAT',
    'TEXTURE_WRAP_CLAMP',
    'TEXTURE_WRAP_MIRROR_REPEAT',
    'TEXTURE_WRAP_MIRROR_CLAMP',

    'CubemapLayout',
    'CUBEMAP_LAYOUT_AUTO_DETECT',
    'CUBEMAP_LAYOUT_LINE_VERTICAL',
    'CUBEMAP_LAYOUT_LINE_HORIZONTAL',
    'CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR',
    'CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE',
    'CUBEMAP_LAYOUT_PANORAMA',

    'FontType',
    'FONT_DEFAULT',
    'FONT_BITMAP',
    'FONT_SDF',

    'BlendMode',
    'BLEND_ALPHA',
    'BLEND_ADDITIVE',
    'BLEND_MULTIPLIED',
    'BLEND_ADD_COLORS',
    'BLEND_SUBTRACT_COLORS',
    'BLEND_CUSTOM',

    'Gesture',
    'GESTURE_NONE',
    'GESTURE_TAP',
    'GESTURE_DOUBLETAP',
    'GESTURE_HOLD',
    'GESTURE_DRAG',
    'GESTURE_SWIPE_RIGHT',
    'GESTURE_SWIPE_LEFT',
    'GESTURE_SWIPE_UP',
    'GESTURE_SWIPE_DOWN',
    'GESTURE_PINCH_IN',
    'GESTURE_PINCH_OUT',

    'CameraMode',
    'CAMERA_CUSTOM',
    'CAMERA_FREE',
    'CAMERA_ORBITAL',
    'CAMERA_FIRST_PERSON',
    'CAMERA_THIRD_PERSON',

    'CameraProjection',
    'CAMERA_PERSPECTIVE',
    'CAMERA_PROJECTION',

    'NPatchLayout',
    'NPATCH_NINE_PATCH',
    'NPATCH_THREE_PATCH_VERTICAL',
    'NPATCH_THREE_PATCH_HORIZONTAL',
]


# ---------------------------------------------------------------------------------
# region ENUMERATORS DEFINITION
# ---------------------------------------------------------------------------------


class ConfigFlags(IntFlag):
    FLAG_VSYNC_HINT = 0x00000040
    FLAG_FULLSCREEN_MODE = 0x00000002
    FLAG_WINDOW_RESIZABLE = 0x00000004
    FLAG_WINDOW_UNDECORATED = 0x00000008
    FLAG_WINDOW_HIDDEN = 0x00000080
    FLAG_WINDOW_MINIMIZED = 0x00000200
    FLAG_WINDOW_MAXIMIZED = 0x00000400
    FLAG_WINDOW_UNFOCUSED = 0x00000800
    FLAG_WINDOW_TOPMOST = 0x00001000
    FLAG_WINDOW_ALWAYS_RUN = 0x00000100
    FLAG_WINDOW_TRANSPARENT = 0x00000010
    FLAG_WINDOW_HIGHDPI = 0x00002000
    FLAG_MSAA_4X_HINT = 0x00000020
    FLAG_INTERLACED_HINT = 0x00010000


FLAG_VSYNC_HINT = ConfigFlags.FLAG_VSYNC_HINT
FLAG_FULLSCREEN_MODE = ConfigFlags.FLAG_FULLSCREEN_MODE
FLAG_WINDOW_RESIZABLE = ConfigFlags.FLAG_WINDOW_RESIZABLE
FLAG_WINDOW_UNDECORATED = ConfigFlags.FLAG_WINDOW_UNDECORATED
FLAG_WINDOW_HIDDEN = ConfigFlags.FLAG_WINDOW_HIDDEN
FLAG_WINDOW_MINIMIZED = ConfigFlags.FLAG_WINDOW_MINIMIZED
FLAG_WINDOW_MAXIMIZED = ConfigFlags.FLAG_WINDOW_MAXIMIZED
FLAG_WINDOW_UNFOCUSED = ConfigFlags.FLAG_WINDOW_UNFOCUSED
FLAG_WINDOW_TOPMOST = ConfigFlags.FLAG_WINDOW_TOPMOST
FLAG_WINDOW_ALWAYS_RUN = ConfigFlags.FLAG_WINDOW_ALWAYS_RUN
FLAG_WINDOW_TRANSPARENT = ConfigFlags.FLAG_WINDOW_TRANSPARENT
FLAG_WINDOW_HIGHDPI = ConfigFlags.FLAG_WINDOW_HIGHDPI
FLAG_MSAA_4X_HINT = ConfigFlags.FLAG_MSAA_4X_HINT
FLAG_INTERLACED_HINT = ConfigFlags.FLAG_INTERLACED_HINT


# Trace log type
class TraceLogLevel(IntEnum):
    LOG_ALL = 0
    LOG_TRACE = auto()
    LOG_DEBUG = auto()
    LOG_INFO = auto()
    LOG_WARNING = auto()
    LOG_ERROR = auto()
    LOG_FATAL = auto()
    LOG_NONE = auto()


LOG_ALL = TraceLogLevel.LOG_ALL
LOG_TRACE = TraceLogLevel.LOG_TRACE
LOG_DEBUG = TraceLogLevel.LOG_DEBUG
LOG_INFO = TraceLogLevel.LOG_INFO
LOG_WARNING = TraceLogLevel.LOG_WARNING
LOG_ERROR = TraceLogLevel.LOG_ERROR
LOG_FATAL = TraceLogLevel.LOG_FATAL
LOG_NONE = TraceLogLevel.LOG_NONE


class KeyboardKey(IntEnum):
    KEY_NULL = 0
    # Alphanumeric keys
    KEY_APOSTROPHE = 39
    KEY_COMMA = 44
    KEY_MINUS = 45
    KEY_PERIOD = 46
    KEY_SLASH = 47
    KEY_ZERO = 48
    KEY_ONE = 49
    KEY_TWO = 50
    KEY_THREE = 51
    KEY_FOUR = 52
    KEY_FIVE = 53
    KEY_SIX = 54
    KEY_SEVEN = 55
    KEY_EIGHT = 56
    KEY_NINE = 57
    KEY_SEMICOLON = 59
    KEY_EQUAL = 61
    KEY_A = 65
    KEY_B = 66
    KEY_C = 67
    KEY_D = 68
    KEY_E = 69
    KEY_F = 70
    KEY_G = 71
    KEY_H = 72
    KEY_I = 73
    KEY_J = 74
    KEY_K = 75
    KEY_L = 76
    KEY_M = 77
    KEY_N = 78
    KEY_O = 79
    KEY_P = 80
    KEY_Q = 81
    KEY_R = 82
    KEY_S = 83
    KEY_T = 84
    KEY_U = 85
    KEY_V = 86
    KEY_W = 87
    KEY_X = 88
    KEY_Y = 89
    KEY_Z = 90

    # Function keys
    KEY_SPACE = 32
    KEY_ESCAPE = 256
    KEY_ENTER = 257
    KEY_TAB = 258
    KEY_BACKSPACE = 259
    KEY_INSERT = 260
    KEY_DELETE = 261
    KEY_RIGHT = 262
    KEY_LEFT = 263
    KEY_DOWN = 264
    KEY_UP = 265
    KEY_PAGE_UP = 266
    KEY_PAGE_DOWN = 267
    KEY_HOME = 268
    KEY_END = 269
    KEY_CAPS_LOCK = 280
    KEY_SCROLL_LOCK = 281
    KEY_NUM_LOCK = 282
    KEY_PRINT_SCREEN = 283
    KEY_PAUSE = 284
    KEY_F1 = 290
    KEY_F2 = 291
    KEY_F3 = 292
    KEY_F4 = 293
    KEY_F5 = 294
    KEY_F6 = 295
    KEY_F7 = 296
    KEY_F8 = 297
    KEY_F9 = 298
    KEY_F10 = 299
    KEY_F11 = 300
    KEY_F12 = 301
    KEY_LEFT_SHIFT = 340
    KEY_LEFT_CONTROL = 341
    KEY_LEFT_ALT = 342
    KEY_LEFT_SUPER = 343
    KEY_RIGHT_SHIFT = 344
    KEY_RIGHT_CONTROL = 345
    KEY_RIGHT_ALT = 346
    KEY_RIGHT_SUPER = 347
    KEY_KB_MENU = 348
    KEY_LEFT_BRACKET = 91
    KEY_BACKSLASH = 92
    KEY_RIGHT_BRACKET = 93
    KEY_GRAVE = 96

    # Keypad keys
    KEY_KP_0 = 320
    KEY_KP_1 = 321
    KEY_KP_2 = 322
    KEY_KP_3 = 323
    KEY_KP_4 = 324
    KEY_KP_5 = 325
    KEY_KP_6 = 326
    KEY_KP_7 = 327
    KEY_KP_8 = 328
    KEY_KP_9 = 329
    KEY_KP_DECIMAL = 330
    KEY_KP_DIVIDE = 331
    KEY_KP_MULTIPLY = 332
    KEY_KP_SUBTRACT = 333
    KEY_KP_ADD = 334
    KEY_KP_ENTER = 335
    KEY_KP_EQUAL = 336
    # Android key buttons
    KEY_BACK = 4
    KEY_MENU = 82
    KEY_VOLUME_UP = 24
    KEY_VOLUME_DOWN = 25


KEY_NULL = KeyboardKey.KEY_NULL
KEY_APOSTROPHE = KeyboardKey.KEY_APOSTROPHE
KEY_COMMA = KeyboardKey.KEY_COMMA
KEY_MINUS = KeyboardKey.KEY_MINUS
KEY_PERIOD = KeyboardKey.KEY_PERIOD
KEY_SLASH = KeyboardKey.KEY_SLASH
KEY_ZERO = KeyboardKey.KEY_ZERO
KEY_ONE = KeyboardKey.KEY_ONE
KEY_TWO = KeyboardKey.KEY_TWO
KEY_THREE = KeyboardKey.KEY_THREE
KEY_FOUR = KeyboardKey.KEY_FOUR
KEY_FIVE = KeyboardKey.KEY_FIVE
KEY_SIX = KeyboardKey.KEY_SIX
KEY_SEVEN = KeyboardKey.KEY_SEVEN
KEY_EIGHT = KeyboardKey.KEY_EIGHT
KEY_NINE = KeyboardKey.KEY_NINE
KEY_SEMICOLON = KeyboardKey.KEY_SEMICOLON
KEY_EQUAL = KeyboardKey.KEY_EQUAL
KEY_A = KeyboardKey.KEY_A
KEY_B = KeyboardKey.KEY_B
KEY_C = KeyboardKey.KEY_C
KEY_D = KeyboardKey.KEY_D
KEY_E = KeyboardKey.KEY_E
KEY_F = KeyboardKey.KEY_F
KEY_G = KeyboardKey.KEY_G
KEY_H = KeyboardKey.KEY_H
KEY_I = KeyboardKey.KEY_I
KEY_J = KeyboardKey.KEY_J
KEY_K = KeyboardKey.KEY_K
KEY_L = KeyboardKey.KEY_L
KEY_M = KeyboardKey.KEY_M
KEY_N = KeyboardKey.KEY_N
KEY_O = KeyboardKey.KEY_O
KEY_P = KeyboardKey.KEY_P
KEY_Q = KeyboardKey.KEY_Q
KEY_R = KeyboardKey.KEY_R
KEY_S = KeyboardKey.KEY_S
KEY_T = KeyboardKey.KEY_T
KEY_U = KeyboardKey.KEY_U
KEY_V = KeyboardKey.KEY_V
KEY_W = KeyboardKey.KEY_W
KEY_X = KeyboardKey.KEY_X
KEY_Y = KeyboardKey.KEY_Y
KEY_Z = KeyboardKey.KEY_Z
KEY_SPACE = KeyboardKey.KEY_SPACE
KEY_ESCAPE = KeyboardKey.KEY_ESCAPE
KEY_ENTER = KeyboardKey.KEY_ENTER
KEY_TAB = KeyboardKey.KEY_TAB
KEY_BACKSPACE = KeyboardKey.KEY_BACKSPACE
KEY_INSERT = KeyboardKey.KEY_INSERT
KEY_DELETE = KeyboardKey.KEY_DELETE
KEY_RIGHT = KeyboardKey.KEY_RIGHT
KEY_LEFT = KeyboardKey.KEY_LEFT
KEY_DOWN = KeyboardKey.KEY_DOWN
KEY_UP = KeyboardKey.KEY_UP
KEY_PAGE_UP = KeyboardKey.KEY_PAGE_UP
KEY_PAGE_DOWN = KeyboardKey.KEY_PAGE_DOWN
KEY_HOME = KeyboardKey.KEY_HOME
KEY_END = KeyboardKey.KEY_END
KEY_CAPS_LOCK = KeyboardKey.KEY_CAPS_LOCK
KEY_SCROLL_LOCK = KeyboardKey.KEY_SCROLL_LOCK
KEY_NUM_LOCK = KeyboardKey.KEY_NUM_LOCK
KEY_PRINT_SCREEN = KeyboardKey.KEY_PRINT_SCREEN
KEY_PAUSE = KeyboardKey.KEY_PAUSE
KEY_F1 = KeyboardKey.KEY_F1
KEY_F2 = KeyboardKey.KEY_F2
KEY_F3 = KeyboardKey.KEY_F3
KEY_F4 = KeyboardKey.KEY_F4
KEY_F5 = KeyboardKey.KEY_F5
KEY_F6 = KeyboardKey.KEY_F6
KEY_F7 = KeyboardKey.KEY_F7
KEY_F8 = KeyboardKey.KEY_F8
KEY_F9 = KeyboardKey.KEY_F9
KEY_F10 = KeyboardKey.KEY_F10
KEY_F11 = KeyboardKey.KEY_F11
KEY_F12 = KeyboardKey.KEY_F12
KEY_LEFT_SHIFT = KeyboardKey.KEY_LEFT_SHIFT
KEY_LEFT_CONTROL = KeyboardKey.KEY_LEFT_CONTROL
KEY_LEFT_ALT = KeyboardKey.KEY_LEFT_ALT
KEY_LEFT_SUPER = KeyboardKey.KEY_LEFT_SUPER
KEY_RIGHT_SHIFT = KeyboardKey.KEY_RIGHT_SHIFT
KEY_RIGHT_CONTROL = KeyboardKey.KEY_RIGHT_CONTROL
KEY_RIGHT_ALT = KeyboardKey.KEY_RIGHT_ALT
KEY_RIGHT_SUPER = KeyboardKey.KEY_RIGHT_SUPER
KEY_KB_MENU = KeyboardKey.KEY_KB_MENU
KEY_LEFT_BRACKET = KeyboardKey.KEY_LEFT_BRACKET
KEY_BACKSLASH = KeyboardKey.KEY_BACKSLASH
KEY_RIGHT_BRACKET = KeyboardKey.KEY_RIGHT_BRACKET
KEY_GRAVE = KeyboardKey.KEY_GRAVE
KEY_KP_0 = KeyboardKey.KEY_KP_0
KEY_KP_1 = KeyboardKey.KEY_KP_1
KEY_KP_2 = KeyboardKey.KEY_KP_2
KEY_KP_3 = KeyboardKey.KEY_KP_3
KEY_KP_4 = KeyboardKey.KEY_KP_4
KEY_KP_5 = KeyboardKey.KEY_KP_5
KEY_KP_6 = KeyboardKey.KEY_KP_6
KEY_KP_7 = KeyboardKey.KEY_KP_7
KEY_KP_8 = KeyboardKey.KEY_KP_8
KEY_KP_9 = KeyboardKey.KEY_KP_9
KEY_KP_DECIMAL = KeyboardKey.KEY_KP_DECIMAL
KEY_KP_DIVIDE = KeyboardKey.KEY_KP_DIVIDE
KEY_KP_MULTIPLY = KeyboardKey.KEY_KP_MULTIPLY
KEY_KP_SUBTRACT = KeyboardKey.KEY_KP_SUBTRACT
KEY_KP_ADD = KeyboardKey.KEY_KP_ADD
KEY_KP_ENTER = KeyboardKey.KEY_KP_ENTER
KEY_KP_EQUAL = KeyboardKey.KEY_KP_EQUAL
KEY_BACK = KeyboardKey.KEY_BACK
KEY_MENU = KeyboardKey.KEY_MENU
KEY_VOLUME_UP = KeyboardKey.KEY_VOLUME_UP
KEY_VOLUME_DOWN = KeyboardKey.KEY_VOLUME_DOWN


class MouseButton(IntEnum):
    MOUSE_BUTTON_LEFT = 0
    MOUSE_BUTTON_RIGHT = 1
    MOUSE_BUTTON_MIDDLE = 2


MOUSE_BUTTON_LEFT = MouseButton.MOUSE_BUTTON_LEFT
MOUSE_BUTTON_RIGHT = MouseButton.MOUSE_BUTTON_RIGHT
MOUSE_BUTTON_MIDDLE = MouseButton.MOUSE_BUTTON_MIDDLE


class MouseCursor(IntEnum):
    MOUSE_CURSOR_DEFAULT = 0
    MOUSE_CURSOR_ARROW = 1
    MOUSE_CURSOR_IBEAM = 2
    MOUSE_CURSOR_CROSSHAIR = 3
    MOUSE_CURSOR_POINTING_HAND = 4
    MOUSE_CURSOR_RESIZE_EW = 5
    MOUSE_CURSOR_RESIZE_NS = 6
    MOUSE_CURSOR_RESIZE_NWSE = 7
    MOUSE_CURSOR_RESIZE_NESW = 8
    MOUSE_CURSOR_RESIZE_ALL = 9
    MOUSE_CURSOR_NOT_ALLOWED = 10


MOUSE_CURSOR_DEFAULT = MouseCursor.MOUSE_CURSOR_DEFAULT
MOUSE_CURSOR_ARROW = MouseCursor.MOUSE_CURSOR_ARROW
MOUSE_CURSOR_IBEAM = MouseCursor.MOUSE_CURSOR_IBEAM
MOUSE_CURSOR_CROSSHAIR = MouseCursor.MOUSE_CURSOR_CROSSHAIR
MOUSE_CURSOR_POINTING_HAND = MouseCursor.MOUSE_CURSOR_POINTING_HAND
MOUSE_CURSOR_RESIZE_EW = MouseCursor.MOUSE_CURSOR_RESIZE_EW
MOUSE_CURSOR_RESIZE_NS = MouseCursor.MOUSE_CURSOR_RESIZE_NS
MOUSE_CURSOR_RESIZE_NWSE = MouseCursor.MOUSE_CURSOR_RESIZE_NWSE
MOUSE_CURSOR_RESIZE_NESW = MouseCursor.MOUSE_CURSOR_RESIZE_NESW
MOUSE_CURSOR_RESIZE_ALL = MouseCursor.MOUSE_CURSOR_RESIZE_ALL
MOUSE_CURSOR_NOT_ALLOWED = MouseCursor.MOUSE_CURSOR_NOT_ALLOWED


class GamepadButton(IntEnum):
    # This is here just for error checking
    GAMEPAD_BUTTON_UNKNOWN = 0,

    # This is normally a DPAD
    GAMEPAD_BUTTON_LEFT_FACE_UP = auto()
    GAMEPAD_BUTTON_LEFT_FACE_RIGHT = auto()
    GAMEPAD_BUTTON_LEFT_FACE_DOWN = auto()
    GAMEPAD_BUTTON_LEFT_FACE_LEFT = auto()

    # This normally corresponds with PlayStation and Xbox controllers
    # XBOX: [Y, X, A, B]
    # PS3: [Triangle, Square, Cross, Circle]
    # No support for 6 button controllers though..
    GAMEPAD_BUTTON_RIGHT_FACE_UP = auto()
    GAMEPAD_BUTTON_RIGHT_FACE_RIGHT = auto()
    GAMEPAD_BUTTON_RIGHT_FACE_DOWN = auto()
    GAMEPAD_BUTTON_RIGHT_FACE_LEFT = auto()

    # Triggers
    GAMEPAD_BUTTON_LEFT_TRIGGER_1 = auto()
    GAMEPAD_BUTTON_LEFT_TRIGGER_2 = auto()
    GAMEPAD_BUTTON_RIGHT_TRIGGER_1 = auto()
    GAMEPAD_BUTTON_RIGHT_TRIGGER_2 = auto()

    # These are buttons in the center of the gamepad
    GAMEPAD_BUTTON_MIDDLE_LEFT = auto()  # PS3 Select
    GAMEPAD_BUTTON_MIDDLE = auto()  # PS Button / XBOX Button
    GAMEPAD_BUTTON_MIDDLE_RIGHT = auto()  # PS3 Start

    # These are the joystick press in buttons
    GAMEPAD_BUTTON_LEFT_THUMB = auto()
    GAMEPAD_BUTTON_RIGHT_THUMB = auto()


GAMEPAD_BUTTON_UNKNOWN = GamepadButton.GAMEPAD_BUTTON_UNKNOWN
GAMEPAD_BUTTON_LEFT_FACE_UP = GamepadButton.GAMEPAD_BUTTON_LEFT_FACE_UP
GAMEPAD_BUTTON_LEFT_FACE_RIGHT = GamepadButton.GAMEPAD_BUTTON_LEFT_FACE_RIGHT
GAMEPAD_BUTTON_LEFT_FACE_DOWN = GamepadButton.GAMEPAD_BUTTON_LEFT_FACE_DOWN
GAMEPAD_BUTTON_LEFT_FACE_LEFT = GamepadButton.GAMEPAD_BUTTON_LEFT_FACE_LEFT
GAMEPAD_BUTTON_RIGHT_FACE_UP = GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_UP
GAMEPAD_BUTTON_RIGHT_FACE_RIGHT = GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_RIGHT
GAMEPAD_BUTTON_RIGHT_FACE_DOWN = GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_DOWN
GAMEPAD_BUTTON_RIGHT_FACE_LEFT = GamepadButton.GAMEPAD_BUTTON_RIGHT_FACE_LEFT
GAMEPAD_BUTTON_LEFT_TRIGGER_1 = GamepadButton.GAMEPAD_BUTTON_LEFT_TRIGGER_1
GAMEPAD_BUTTON_LEFT_TRIGGER_2 = GamepadButton.GAMEPAD_BUTTON_LEFT_TRIGGER_2
GAMEPAD_BUTTON_RIGHT_TRIGGER_1 = GamepadButton.GAMEPAD_BUTTON_RIGHT_TRIGGER_1
GAMEPAD_BUTTON_RIGHT_TRIGGER_2 = GamepadButton.GAMEPAD_BUTTON_RIGHT_TRIGGER_2
GAMEPAD_BUTTON_MIDDLE_LEFT = GamepadButton.GAMEPAD_BUTTON_MIDDLE_LEFT
GAMEPAD_BUTTON_MIDDLE = GamepadButton.GAMEPAD_BUTTON_MIDDLE
GAMEPAD_BUTTON_MIDDLE_RIGHT = GamepadButton.GAMEPAD_BUTTON_MIDDLE_RIGHT
GAMEPAD_BUTTON_LEFT_THUMB = GamepadButton.GAMEPAD_BUTTON_LEFT_THUMB
GAMEPAD_BUTTON_RIGHT_THUMB = GamepadButton.GAMEPAD_BUTTON_RIGHT_THUMB


# Gamepad axis
class GamepadAxis(IntEnum):
    # Left stick
    GAMEPAD_AXIS_LEFT_X = 0
    GAMEPAD_AXIS_LEFT_Y = 1

    # Right stick
    GAMEPAD_AXIS_RIGHT_X = 2
    GAMEPAD_AXIS_RIGHT_Y = 3

    # Pressure levels for the back triggers
    GAMEPAD_AXIS_LEFT_TRIGGER = 4  # [1..-1] (pressure-level)
    GAMEPAD_AXIS_RIGHT_TRIGGER = 5  # [1..-1] (pressure-level)


GAMEPAD_AXIS_LEFT_X = GamepadAxis.GAMEPAD_AXIS_LEFT_X
GAMEPAD_AXIS_LEFT_Y = GamepadAxis.GAMEPAD_AXIS_LEFT_Y
GAMEPAD_AXIS_RIGHT_X = GamepadAxis.GAMEPAD_AXIS_RIGHT_X
GAMEPAD_AXIS_RIGHT_Y = GamepadAxis.GAMEPAD_AXIS_RIGHT_Y
GAMEPAD_AXIS_LEFT_TRIGGER = GamepadAxis.GAMEPAD_AXIS_LEFT_TRIGGER
GAMEPAD_AXIS_RIGHT_TRIGGER = GamepadAxis.GAMEPAD_AXIS_RIGHT_TRIGGER


class MaterialMapIndex(IntEnum):
    MATERIAL_MAP_ALBEDO = 0  # MATERIAL_MAP_DIFFUSE
    MATERIAL_MAP_METALNESS = 1  # MATERIAL_MAP_SPECULAR
    MATERIAL_MAP_NORMAL = 2
    MATERIAL_MAP_ROUGHNESS = 3
    MATERIAL_MAP_OCCLUSION = auto()
    MATERIAL_MAP_EMISSION = auto()
    MATERIAL_MAP_HEIGHT = auto()
    MATERIAL_MAP_BRDG = auto()
    MATERIAL_MAP_CUBEMAP = auto()  # Uses GL_TEXTURE_CUBE_MAP
    MATERIAL_MAP_IRRADIANCE = auto()  # Uses GL_TEXTURE_CUBE_MAP
    MATERIAL_MAP_PREFILTER = auto()  # Uses GL_TEXTURE_CUBE_MAP


MATERIAL_MAP_ALBEDO = MaterialMapIndex.MATERIAL_MAP_ALBEDO
MATERIAL_MAP_METALNESS = MaterialMapIndex.MATERIAL_MAP_METALNESS
MATERIAL_MAP_NORMAL = MaterialMapIndex.MATERIAL_MAP_NORMAL
MATERIAL_MAP_ROUGHNESS = MaterialMapIndex.MATERIAL_MAP_ROUGHNESS
MATERIAL_MAP_OCCLUSION = MaterialMapIndex.MATERIAL_MAP_OCCLUSION
MATERIAL_MAP_EMISSION = MaterialMapIndex.MATERIAL_MAP_EMISSION
MATERIAL_MAP_HEIGHT = MaterialMapIndex.MATERIAL_MAP_HEIGHT
MATERIAL_MAP_BRDG = MaterialMapIndex.MATERIAL_MAP_BRDG
MATERIAL_MAP_CUBEMAP = MaterialMapIndex.MATERIAL_MAP_CUBEMAP
MATERIAL_MAP_IRRADIANCE = MaterialMapIndex.MATERIAL_MAP_IRRADIANCE
MATERIAL_MAP_PREFILTER = MaterialMapIndex.MATERIAL_MAP_PREFILTER
MATERIAL_MAP_DIFFUSE = MaterialMapIndex.MATERIAL_MAP_ALBEDO
MATERIAL_MAP_SPECULAR = MaterialMapIndex.MATERIAL_MAP_METALNESS


class ShaderLocationIndex(IntEnum):
    SHADER_LOC_VERTEX_POSITION = 0
    SHADER_LOC_VERTEX_TEXCOORD01 = auto()
    SHADER_LOC_VERTEX_TEXCOORD02 = auto()
    SHADER_LOC_VERTEX_NORMAL = auto()
    SHADER_LOC_VERTEX_TANGENT = auto()
    SHADER_LOC_VERTEX_COLOR = auto()
    SHADER_LOC_MATRIX_MVP = auto()
    SHADER_LOC_MATRIX_VIEW = auto()
    SHADER_LOC_MATRIX_PROJECTION = auto()
    SHADER_LOC_MATRIX_MODEL = auto()
    SHADER_LOC_MATRIX_NORMAL = auto()
    SHADER_LOC_VECTOR_VIEW = auto()
    SHADER_LOC_COLOR_DIFFUSE = auto()
    SHADER_LOC_COLOR_SPECULAR = auto()
    SHADER_LOC_COLOR_AMBIENT = auto()
    SHADER_LOC_MAP_ALBEDO = auto()  # SHADER_LOC_MAP_DIFFUSE
    SHADER_LOC_MAP_METALNESS = auto()  # SHADER_LOC_MAP_SPECULAR
    SHADER_LOC_MAP_NORMAL = auto()
    SHADER_LOC_MAP_ROUGHNESS = auto()
    SHADER_LOC_MAP_OCCLUSION = auto()
    SHADER_LOC_MAP_EMISSION = auto()
    SHADER_LOC_MAP_HEIGHT = auto()
    SHADER_LOC_MAP_CUBEMAP = auto()
    SHADER_LOC_MAP_IRRADIANCE = auto()
    SHADER_LOC_MAP_PREFILTER = auto()
    SHADER_LOC_MAP_BRDF = auto()


SHADER_LOC_VERTEX_POSITION = ShaderLocationIndex.SHADER_LOC_VERTEX_POSITION
SHADER_LOC_VERTEX_TEXCOORD01 = ShaderLocationIndex.SHADER_LOC_VERTEX_TEXCOORD01
SHADER_LOC_VERTEX_TEXCOORD02 = ShaderLocationIndex.SHADER_LOC_VERTEX_TEXCOORD02
SHADER_LOC_VERTEX_NORMAL = ShaderLocationIndex.SHADER_LOC_VERTEX_NORMAL
SHADER_LOC_VERTEX_TANGENT = ShaderLocationIndex.SHADER_LOC_VERTEX_TANGENT
SHADER_LOC_VERTEX_COLOR = ShaderLocationIndex.SHADER_LOC_VERTEX_COLOR
SHADER_LOC_MATRIX_MVP = ShaderLocationIndex.SHADER_LOC_MATRIX_MVP
SHADER_LOC_MATRIX_VIEW = ShaderLocationIndex.SHADER_LOC_MATRIX_VIEW
SHADER_LOC_MATRIX_PROJECTION = ShaderLocationIndex.SHADER_LOC_MATRIX_PROJECTION
SHADER_LOC_MATRIX_MODEL = ShaderLocationIndex.SHADER_LOC_MATRIX_MODEL
SHADER_LOC_MATRIX_NORMAL = ShaderLocationIndex.SHADER_LOC_MATRIX_NORMAL
SHADER_LOC_VECTOR_VIEW = ShaderLocationIndex.SHADER_LOC_VECTOR_VIEW
SHADER_LOC_COLOR_DIFFUSE = ShaderLocationIndex.SHADER_LOC_COLOR_DIFFUSE
SHADER_LOC_COLOR_SPECULAR = ShaderLocationIndex.SHADER_LOC_COLOR_SPECULAR
SHADER_LOC_COLOR_AMBIENT = ShaderLocationIndex.SHADER_LOC_COLOR_AMBIENT
SHADER_LOC_MAP_ALBEDO = ShaderLocationIndex.SHADER_LOC_MAP_ALBEDO
SHADER_LOC_MAP_METALNESS = ShaderLocationIndex.SHADER_LOC_MAP_METALNESS
SHADER_LOC_MAP_NORMAL = ShaderLocationIndex.SHADER_LOC_MAP_NORMAL
SHADER_LOC_MAP_ROUGHNESS = ShaderLocationIndex.SHADER_LOC_MAP_ROUGHNESS
SHADER_LOC_MAP_OCCLUSION = ShaderLocationIndex.SHADER_LOC_MAP_OCCLUSION
SHADER_LOC_MAP_EMISSION = ShaderLocationIndex.SHADER_LOC_MAP_EMISSION
SHADER_LOC_MAP_HEIGHT = ShaderLocationIndex.SHADER_LOC_MAP_HEIGHT
SHADER_LOC_MAP_CUBEMAP = ShaderLocationIndex.SHADER_LOC_MAP_CUBEMAP
SHADER_LOC_MAP_IRRADIANCE = ShaderLocationIndex.SHADER_LOC_MAP_IRRADIANCE
SHADER_LOC_MAP_PREFILTER = ShaderLocationIndex.SHADER_LOC_MAP_PREFILTER
SHADER_LOC_MAP_BRDF = ShaderLocationIndex.SHADER_LOC_MAP_BRDF
SHADER_LOC_MAP_DIFFUSE = SHADER_LOC_MAP_ALBEDO
SHADER_LOC_MAP_SPECULAR = SHADER_LOC_MAP_METALNESS


class ShaderUniformDataType(IntEnum):
    SHADER_UNIFORM_FLOAT = 0,
    SHADER_UNIFORM_VEC2 = auto()
    SHADER_UNIFORM_VEC3 = auto()
    SHADER_UNIFORM_VEC4 = auto()
    SHADER_UNIFORM_INT = auto()
    SHADER_UNIFORM_IVEC2 = auto()
    SHADER_UNIFORM_IVEC3 = auto()
    SHADER_UNIFORM_IVEC4 = auto()
    SHADER_UNIFORM_SAMPLER2D = auto()


SHADER_UNIFORM_FLOAT = ShaderUniformDataType.SHADER_UNIFORM_FLOAT
SHADER_UNIFORM_VEC2 = ShaderUniformDataType.SHADER_UNIFORM_VEC2
SHADER_UNIFORM_VEC3 = ShaderUniformDataType.SHADER_UNIFORM_VEC3
SHADER_UNIFORM_VEC4 = ShaderUniformDataType.SHADER_UNIFORM_VEC4
SHADER_UNIFORM_INT = ShaderUniformDataType.SHADER_UNIFORM_INT
SHADER_UNIFORM_IVEC2 = ShaderUniformDataType.SHADER_UNIFORM_IVEC2
SHADER_UNIFORM_IVEC3 = ShaderUniformDataType.SHADER_UNIFORM_IVEC3
SHADER_UNIFORM_IVEC4 = ShaderUniformDataType.SHADER_UNIFORM_IVEC4
SHADER_UNIFORM_SAMPLER2D = ShaderUniformDataType.SHADER_UNIFORM_SAMPLER2D


class PixelFormat(IntEnum):
    PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = 1  # 8 bit per pixel (no alpha)
    PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = auto()  # 8*2 bpp (2 channels)
    PIXELFORMAT_UNCOMPRESSED_R5G6B5 = auto()  # 16 bpp
    PIXELFORMAT_UNCOMPRESSED_R8G8B8 = auto()  # 24 bpp
    PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = auto()  # 16 bpp (1 bit alpha)
    PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = auto()  # 16 bpp (4 bit alpha)
    PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = auto()  # 32 bpp
    PIXELFORMAT_UNCOMPRESSED_R32 = auto()  # 32 bpp (1 channel - float)
    PIXELFORMAT_UNCOMPRESSED_R32G32B32 = auto()  # 32*3 bpp (3 channels - float)
    PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = auto()  # 32*4 bpp (4 channels - float)
    PIXELFORMAT_COMPRESSED_DXT1_RGB = auto()  # 4 bpp (no alpha)
    PIXELFORMAT_COMPRESSED_DXT1_RGBA = auto()  # 4 bpp (1 bit alpha)
    PIXELFORMAT_COMPRESSED_DXT3_RGBA = auto()  # 8 bpp
    PIXELFORMAT_COMPRESSED_DXT5_RGBA = auto()  # 8 bpp
    PIXELFORMAT_COMPRESSED_ETC1_RGB = auto()  # 4 bpp
    PIXELFORMAT_COMPRESSED_ETC2_RGB = auto()  # 4 bpp
    PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = auto()  # 8 bpp
    PIXELFORMAT_COMPRESSED_PVRT_RGB = auto()  # 4 bpp
    PIXELFORMAT_COMPRESSED_PVRT_RGBA = auto()  # 4 bpp
    PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = auto()  # 8 bpp
    PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = auto()  # 2 bpp


PIXELFORMAT_UNCOMPRESSED_GRAYSCALE = PixelFormat.PIXELFORMAT_UNCOMPRESSED_GRAYSCALE
PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA = PixelFormat.PIXELFORMAT_UNCOMPRESSED_GRAY_ALPHA
PIXELFORMAT_UNCOMPRESSED_R5G6B5 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R5G6B5
PIXELFORMAT_UNCOMPRESSED_R8G8B8 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R8G8B8
PIXELFORMAT_UNCOMPRESSED_R5G5B5A1 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R5G5B5A1
PIXELFORMAT_UNCOMPRESSED_R4G4B4A4 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R4G4B4A4
PIXELFORMAT_UNCOMPRESSED_R8G8B8A8 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R8G8B8A8
PIXELFORMAT_UNCOMPRESSED_R32 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R32
PIXELFORMAT_UNCOMPRESSED_R32G32B32 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R32G32B32
PIXELFORMAT_UNCOMPRESSED_R32G32B32A32 = PixelFormat.PIXELFORMAT_UNCOMPRESSED_R32G32B32A32
PIXELFORMAT_COMPRESSED_DXT1_RGB = PixelFormat.PIXELFORMAT_COMPRESSED_DXT1_RGB
PIXELFORMAT_COMPRESSED_DXT1_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_DXT1_RGBA
PIXELFORMAT_COMPRESSED_DXT3_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_DXT3_RGBA
PIXELFORMAT_COMPRESSED_DXT5_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_DXT5_RGBA
PIXELFORMAT_COMPRESSED_ETC1_RGB = PixelFormat.PIXELFORMAT_COMPRESSED_ETC1_RGB
PIXELFORMAT_COMPRESSED_ETC2_RGB = PixelFormat.PIXELFORMAT_COMPRESSED_ETC2_RGB
PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_ETC2_EAC_RGBA
PIXELFORMAT_COMPRESSED_PVRT_RGB = PixelFormat.PIXELFORMAT_COMPRESSED_PVRT_RGB
PIXELFORMAT_COMPRESSED_PVRT_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_PVRT_RGBA
PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_ASTC_4x4_RGBA
PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA = PixelFormat.PIXELFORMAT_COMPRESSED_ASTC_8x8_RGBA


class TextureFilter(IntEnum):
    TEXTURE_FILTER_POINT = 0  # No filter, just pixel aproximation
    TEXTURE_FILTER_BILINEAR = auto()  # Linear filtering
    TEXTURE_FILTER_TRILINEAR = auto()  # Trilinear filtering (linear with mipmaps)
    TEXTURE_FILTER_ANISOTROPIC_4X = auto()  # Anisotropic filtering 4x
    TEXTURE_FILTER_ANISOTROPIC_8X = auto()  # Anisotropic filtering 8x
    TEXTURE_FILTER_ANISOTROPIC_16X = auto()  # Anisotropic filtering 16x


TEXTURE_FILTER_POINT = TextureFilter.TEXTURE_FILTER_POINT
TEXTURE_FILTER_BILINEAR = TextureFilter.TEXTURE_FILTER_BILINEAR
TEXTURE_FILTER_TRILINEAR = TextureFilter.TEXTURE_FILTER_TRILINEAR
TEXTURE_FILTER_ANISOTROPIC_4X = TextureFilter.TEXTURE_FILTER_ANISOTROPIC_4X
TEXTURE_FILTER_ANISOTROPIC_8X = TextureFilter.TEXTURE_FILTER_ANISOTROPIC_8X
TEXTURE_FILTER_ANISOTROPIC_16X = TextureFilter.TEXTURE_FILTER_ANISOTROPIC_16X


class TextureWrap(IntEnum):
    TEXTURE_WRAP_REPEAT = 0  # Repeats texture in tiled mode
    TEXTURE_WRAP_CLAMP = auto()  # Clamps texture to edge pixel in tiled mode
    TEXTURE_WRAP_MIRROR_REPEAT = auto()  # Mirrors and repeats the texture in tiled mode
    TEXTURE_WRAP_MIRROR_CLAMP = auto()  # Mirrors and clamps to border the texture in tiled mode


TEXTURE_WRAP_REPEAT = TextureWrap.TEXTURE_WRAP_REPEAT
TEXTURE_WRAP_CLAMP = TextureWrap.TEXTURE_WRAP_CLAMP
TEXTURE_WRAP_MIRROR_REPEAT = TextureWrap.TEXTURE_WRAP_MIRROR_REPEAT
TEXTURE_WRAP_MIRROR_CLAMP = TextureWrap.TEXTURE_WRAP_MIRROR_CLAMP


class CubemapLayout(IntEnum):
    CUBEMAP_LAYOUT_AUTO_DETECT = 0  # Automatically detect layout type
    CUBEMAP_LAYOUT_LINE_VERTICAL = auto()  # Layout is defined by a vertical line with faces
    CUBEMAP_LAYOUT_LINE_HORIZONTAL = auto()  # Layout is defined by an horizontal line with faces
    CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR = auto()  # Layout is defined by a 3x4 cross with cubemap faces
    CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE = auto()  # Layout is defined by a 4x3 cross with cubemap faces
    CUBEMAP_LAYOUT_PANORAMA = auto()  # Layout is defined by a panorama image (equirectangular map)


CUBEMAP_LAYOUT_AUTO_DETECT = CubemapLayout.CUBEMAP_LAYOUT_AUTO_DETECT
CUBEMAP_LAYOUT_LINE_VERTICAL = CubemapLayout.CUBEMAP_LAYOUT_LINE_VERTICAL
CUBEMAP_LAYOUT_LINE_HORIZONTAL = CubemapLayout.CUBEMAP_LAYOUT_LINE_HORIZONTAL
CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR = CubemapLayout.CUBEMAP_LAYOUT_CROSS_THREE_BY_FOUR
CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE = CubemapLayout.CUBEMAP_LAYOUT_CROSS_FOUR_BY_THREE
CUBEMAP_LAYOUT_PANORAMA = CubemapLayout.CUBEMAP_LAYOUT_PANORAMA


class FontType(IntEnum):
    FONT_DEFAULT = 0  # Default font generation, anti-aliased
    FONT_BITMAP = auto()  # Bitmap font generation, no anti-aliasing
    FONT_SDF = auto()  # SDF font generation, requires external shader


FONT_DEFAULT = FontType.FONT_DEFAULT
FONT_BITMAP = FontType.FONT_BITMAP
FONT_SDF = FontType.FONT_SDF


class BlendMode(IntEnum):
    BLEND_ALPHA = 0  # Blend textures considering alpha (default)
    BLEND_ADDITIVE = auto()  # Blend textures adding colors
    BLEND_MULTIPLIED = auto()  # Blend textures multiplying colors
    BLEND_ADD_COLORS = auto()  # Blend textures adding colors (alternative)
    BLEND_SUBTRACT_COLORS = auto()  # Blend textures subtracting colors (alternative)
    BLEND_CUSTOM = auto()  # Belnd textures using custom src/dst factors (use rlSetBlendMode())


BLEND_ALPHA = BlendMode.BLEND_ALPHA
BLEND_ADDITIVE = BlendMode.BLEND_ADDITIVE
BLEND_MULTIPLIED = BlendMode.BLEND_MULTIPLIED
BLEND_ADD_COLORS = BlendMode.BLEND_ADD_COLORS
BLEND_SUBTRACT_COLORS = BlendMode.BLEND_SUBTRACT_COLORS
BLEND_CUSTOM = BlendMode.BLEND_CUSTOM


class Gesture(IntFlag):
    GESTURE_NONE = 0
    GESTURE_TAP = 1
    GESTURE_DOUBLETAP = 2
    GESTURE_HOLD = 4
    GESTURE_DRAG = 8
    GESTURE_SWIPE_RIGHT = 16
    GESTURE_SWIPE_LEFT = 32
    GESTURE_SWIPE_UP = 64
    GESTURE_SWIPE_DOWN = 128
    GESTURE_PINCH_IN = 256
    GESTURE_PINCH_OUT = 512


GESTURE_NONE = Gesture.GESTURE_NONE
GESTURE_TAP = Gesture.GESTURE_TAP
GESTURE_DOUBLETAP = Gesture.GESTURE_DOUBLETAP
GESTURE_HOLD = Gesture.GESTURE_HOLD
GESTURE_DRAG = Gesture.GESTURE_DRAG
GESTURE_SWIPE_RIGHT = Gesture.GESTURE_SWIPE_RIGHT
GESTURE_SWIPE_LEFT = Gesture.GESTURE_SWIPE_LEFT
GESTURE_SWIPE_UP = Gesture.GESTURE_SWIPE_UP
GESTURE_SWIPE_DOWN = Gesture.GESTURE_SWIPE_DOWN
GESTURE_PINCH_IN = Gesture.GESTURE_PINCH_IN
GESTURE_PINCH_OUT = Gesture.GESTURE_PINCH_OUT


class CameraMode(IntEnum):
    CAMERA_CUSTOM = 0
    CAMERA_FREE = auto()
    CAMERA_ORBITAL = auto()
    CAMERA_FIRST_PERSON = auto()
    CAMERA_THIRD_PERSON = auto()


CAMERA_CUSTOM = CameraMode.CAMERA_CUSTOM
CAMERA_FREE = CameraMode.CAMERA_FREE
CAMERA_ORBITAL = CameraMode.CAMERA_ORBITAL
CAMERA_FIRST_PERSON = CameraMode.CAMERA_FIRST_PERSON
CAMERA_THIRD_PERSON = CameraMode.CAMERA_THIRD_PERSON


class CameraProjection(IntEnum):
    CAMERA_PERSPECTIVE = 0
    CAMERA_PROJECTION = 1


CAMERA_PERSPECTIVE = CameraProjection.CAMERA_PERSPECTIVE
CAMERA_PROJECTION = CameraProjection.CAMERA_PROJECTION


class NPatchLayout(IntEnum):
    NPATCH_NINE_PATCH = 0  # Npatch layout: 3x3 tiles
    NPATCH_THREE_PATCH_VERTICAL = auto()  # Npatch layout: 1x3 tiles
    NPATCH_THREE_PATCH_HORIZONTAL = auto()  # Npatch layout: 3x1 tiles


NPATCH_NINE_PATCH = NPatchLayout.NPATCH_NINE_PATCH
NPATCH_THREE_PATCH_VERTICAL = NPatchLayout.NPATCH_THREE_PATCH_VERTICAL
NPATCH_THREE_PATCH_HORIZONTAL = NPatchLayout.NPATCH_THREE_PATCH_HORIZONTAL


# endregion (enumerators definition)
# -----------------------------------------------------------------------------


def main():
    d = globals()
    for n in d:
        print(n)


if __name__ == '__main__':
    main()
