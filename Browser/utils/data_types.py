# Copyright 2020-     Robot Framework Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum, auto
from typing import Dict

from typing_extensions import TypedDict


def convert_typed_dict(data_type, params: Dict, key: str) -> Dict:
    if key not in params:
        return params
    dictionary = {k.lower(): v for k, v in params[key].items()}
    struct = data_type.__annotations__
    typed_dict = data_type()
    for req_key in data_type.__required_keys__:
        if req_key.lower() not in dictionary:
            raise RuntimeError(
                f"`{dictionary}` cannot be converted to {data_type.__name__}."
                f"\nThe required key '{req_key}' in not set in given value."
                f"\nExpected types: {data_type.__annotations__}"
            )
        typed_dict[req_key] = struct[req_key](dictionary[req_key.lower()])
    for opt_key in data_type.__optional_keys__:
        if opt_key.lower() not in dictionary:
            continue
        typed_dict[opt_key] = struct[opt_key](dictionary[opt_key.lower()])
    params[key] = typed_dict
    return params


class BoundingBox(TypedDict, total=False):
    x: float
    y: float
    width: float
    height: float


class Coordinates(TypedDict, total=False):
    x: float
    y: float


class MouseOptionsDict(TypedDict, total=False):
    x: float
    y: float
    options: dict


class ViewportDimensions(TypedDict):
    width: int
    height: int


class HttpCredentials(TypedDict):
    username: str
    password: str


class _GeoCoordinated(TypedDict):
    longitude: float
    latitude: float


class GeoLocation(_GeoCoordinated, total=False):
    """Defines the geolocation.

    - ``latitude`` Latitude between -90 and 90.
    - ``longitude`` Longitude between -180 and 180.
    - ``accuracy`` *Optional* Non-negative accuracy value. Defaults to 0.
    Example usage: ``{'latitude': 59.95, 'longitude': 30.31667}``"""

    accuracy: float


class _Server(TypedDict):
    server: str


class Proxy(_Server, total=False):
    """Network proxy settings.

    ``server`` Proxy to be used for all requests. HTTP and SOCKS proxies are supported,
     for example http://myproxy.com:3128 or socks5://myproxy.com:3128.
     Short form myproxy.com:3128 is considered an HTTP proxy.

    ``bypass`` *Optional* coma-separated domains to bypass proxy,
    for example ".com, chromium.org, .domain.com".

    ``username`` *Optional* username to use if HTTP proxy requires authentication.

    ``password`` *Optional* password to use if HTTP proxy requires authentication.
    """

    bypass: str
    Username: str
    password: str


class SelectionType(Enum):
    ACTIVE = auto()
    CURRENT = ACTIVE
    ALL = auto()
    ANY = ALL


class DialogAction(Enum):
    accept = auto()
    dismiss = auto()


class CookieType(Enum):
    dictionary = auto()
    dict = dictionary
    string = auto()
    str = string


CookieSameSite = Enum(
    "CookieSameSite", {"Strict": "Strict", "Lax": "Lax", "None": "None"}
)


class RequestMethod(Enum):
    HEAD = auto()
    GET = auto()
    POST = auto()
    PUT = auto()
    PATCH = auto()
    DELETE = auto()


class MouseButtonAction(Enum):
    click = auto()
    down = auto()
    up = auto()


class MouseButton(Enum):
    left = auto()
    middle = auto()
    right = auto()


class KeyAction(Enum):
    down = auto()
    up = auto()
    press = auto()


class KeyboardInputAction(Enum):
    insertText = auto()
    type = auto()


class KeyboardModifier(Enum):
    Alt = auto()
    Control = auto()
    Meta = auto()
    Shift = auto()


class SelectAttribute(Enum):
    value = auto()
    label = auto()
    text = label
    index = auto()


class SupportedBrowsers(Enum):
    chromium = auto()
    firefox = auto()
    webkit = auto()


ColorScheme = Enum("ColorScheme", ["dark", "light", "no-preference"])


ScrollBehavior = Enum("ScrollBehavior", ["auto", "smooth"])


class SizeFields(Enum):
    width = auto()
    height = auto()
    ALL = auto()


class AreaFields(Enum):
    top = auto()
    left = auto()
    bottom = auto()
    right = auto()
    ALL = auto()


class BoundingBoxFields(Enum):
    width = auto()
    height = auto()
    x = auto()
    y = auto()
    ALL = auto()


class AutoClosingLevel(Enum):
    SUITE = auto()
    TEST = auto()
    MANUAL = auto()


class ElementState(Enum):
    attached = auto()
    detached = auto()
    visible = auto()
    hidden = auto()
    enabled = auto()
    disabled = auto()
    editable = auto()
    readonly = auto()
    selected = auto()
    deselected = auto()
    focused = auto()
    defocused = auto()
    checked = auto()
    unchecked = auto()


class ElementStateKey(Enum):
    attached = auto()
    visible = auto()
    disabled = auto()
    readonly = auto()
    selected = auto()
    focused = auto()
    checked = auto()


AssertionOperator = Enum(
    "AssertionOperator",
    {
        "equal": "==",
        "==": "==",
        "should be": "==",
        "inequal": "!=",
        "!=": "!=",
        "should not be": "!=",
        "less than": "<",
        "<": "<",
        "greater than": ">",
        ">": ">",
        "<=": "<=",
        ">=": ">=",
        "contains": "*=",
        "*=": "*=",
        "starts": "^=",
        "^=": "^=",
        "should start with": "^=",
        "ends": "$=",
        "should end with": "$=",
        "$=": "$=",
        "matches": "$",
        "validate": "validate",
        "then": "then",
        "evaluate": "then",
    },
)
