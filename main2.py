"""main2.py - single-file build of the Uber Eats account generator.

This file bundles spoof.py, engine/utils.py, device.py,
engine/account_manager.py, otp_hotmail.py, and main.py into one script.
It is hotmail007-only (no IMAP / catchall path).

External files used at runtime are unchanged:
  - config.json
  - hotmail_accounts.txt
  - proxies.txt
  - genned/*.json
"""



# ======================================================================
# spoof.py
# ======================================================================

import random as rnd
import hashlib as hsh
import time as tme
import base64 as b64
import json as jsn
from datetime import datetime as dtt
from urllib.parse import quote

CCJS_TOKEN = "AU3DAsLmFWtIgqtMtbLbS4w+32SSNYk0AQS9WYyPUuOLhqEUCPK47i3ypCM9lWN66r3bI8CKv6g0/nR1HGPLSmIJz9rr9OvT+yYvqYutAAsCNPB37oDtWKScPMbZkKMekyaAhhoRP7gY4cOXmQp5TLTx600WoD0Ym9qhqZqZ2DgpdECred+9GXB9UX4BJbT0YabTYmtTX5NAHOVB+Gh4gdoeG//nire/I36pWIVWDvrJivw9Apah5BGR/tkoBh8zL9dLXaCKGg2/haK6oADbhHiJGjh0Sw3potxmf3vh/+tjGK9UNSkJqNqgRVdqgxrUP254aleIH7v+TvDcarsjlrSGehsQbJjYYeJT1+bW3YL3PzeLuckP0hNqztGMzmA="
CCJS_TAG = CCJS_TOKEN[:24]
XOR_KEY = [89, 231, 225, 55]

def xor_base64_utf8(payload: str) -> str:
    xored = "".join(chr(ord(ch) ^ XOR_KEY[i % len(XOR_KEY)]) for i, ch in enumerate(payload))
    return b64.b64encode(xored.encode("utf-8")).decode("ascii")

class Pixel9ProSpoof:

    width = 1344
    hei = 2992
    dpr = 3
    cdp = 24
    pde = 24
    awi = 1344
    ahe = 2847
    inw = 448
    inh = 865
    outw = 448
    outh = 949

    def __init__(slf):
        slf.dd = {}
        slf.gen()

    def gen(slf):
        slf.nav()
        slf.scr()
        slf.win()
        slf.ua()
        slf.wgl()
        slf.auc()
        slf.can()
        slf.tim()
        slf.con()
        slf.bat()
        slf.bfe()
        slf.css()
        slf.stg()
        slf.misc()

    def nav(slf):
        ver = "131.0.6778.135"
        av = "15"
        slf.dd.update({
            "navigator.appVersion": f"5.0 (Linux; Android {av}; Pixel 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver} Mobile Safari/537.36",
            "navigator.appName": "Netscape",
            "navigator.product": "Gecko",
            "navigator.platform": "Linux armv8l",
            "navigator.language": "en-US",
            "navigator.userAgent": f"Mozilla/5.0 (Linux; Android {av}; Pixel 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver} Mobile Safari/537.36",
            "navigator.cookieEnabled": True,
            "navigator.hardwareConcurrency": 8,
            "navigator.deviceMemory": 8,
            "navigator.doNotTrack": "null",
            "navigator.automationEnabled": False,
            "navigator.maxTouchPoints": 5,
            "touchEnabled": True,
            "webdriver_detect": False,
            "navigator.vendor": "Google Inc.",
            "navigator.productSub": "20030107",
            "navigator.appCodeName": "Mozilla",
        })

    def scr(slf):
        slf.dd.update({
            "window.screen.colorDepth": str(slf.cdp),
            "window.screen.pixelDepth": str(slf.pde),
            "window.screen.height": str(slf.hei),
            "window.screen.width": str(slf.width),
            "window.screen.availHeight": str(slf.ahe),
            "screen.availWidth": str(slf.awi),
            "screen.availHeight": str(slf.ahe),
            "window.devicePixelRatio": str(slf.dpr),
            "window.screen.orientation.type": "portrait-primary",
            "window.screen.orientation.angle": "0",
            "window.screen.darkMode.enabled": False,
        })

    def win(slf):
        slf.dd.update({
            "window.outerWidth": str(slf.outw),
            "window.outerHeight": str(slf.outh),
            "window.innerWidth": str(slf.inw),
            "window.innerHeight": str(slf.inh),
            "window.history.length": str(rnd.randint(1, 10)),
            "window.clientInformation.language": "en-US",
            "window.doNotTrack": "null",
        })

    def ua(slf):
        ver = "131.0.6778.135"
        slf.dd.update({
            "navigator.userAgentData.brands": [
                {"brand": "Chromium", "version": "131"},
                {"brand": "Google Chrome", "version": "131"},
                {"brand": "Not_A Brand", "version": "24"}
            ],
            "navigator.userAgentData.mobile": True,
            "navigator.userAgentData.platform": "Android",
            "navigator.userAgentData.highEntropyValues.platform": "Android",
            "navigator.userAgentData.highEntropyValues.platformVersion": "15.0.0",
            "navigator.userAgentData.highEntropyValues.architecture": "arm",
            "navigator.userAgentData.highEntropyValues.bitness": "64",
            "navigator.userAgentData.highEntropyValues.model": "Pixel 9 Pro",
            "navigator.userAgentData.highEntropyValues.uaFullVersion": ver,
            "navigator.userAgentData.highEntropyValues.fullVersionList": [
                {"brand": "Chromium", "version": ver},
                {"brand": "Google Chrome", "version": ver},
                {"brand": "Not_A Brand", "version": "24.0.0.0"}
            ],
        })

    def wgl(slf):
        slf.dd.update({
            "webgl-supported": True,
            "webgl-version": "WebGL 1.0 (OpenGL ES 2.0 Chromium)",
            "webgl-glsl-version": "WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)",
            "webgl-vendor": "WebKit",
            "webgl-renderer": "WebKit WebGL",
            "webgl-vendor-real": "ARM",
            "webgl-renderer-real": "Mali-G715-Immortalis MC11",
            "webgl-max-aa": "16",
            "webgl-unmasked-vendor": "ARM",
            "webgl-unmasked-renderer": "ANGLE (ARM, Mali-G715-Immortalis MC11, OpenGL ES 3.2)",
            "webgl-vertex-shader-highp-float": {"rangeMin": 127, "rangeMax": 127, "precision": 23},
            "webgl-vertex-shader-mediump-float": {"rangeMin": 15, "rangeMax": 15, "precision": 10},
            "webgl-fragment-shader-highp-float": {"rangeMin": 127, "rangeMax": 127, "precision": 23},
            "webgl-fragment-shader-mediump-float": {"rangeMin": 15, "rangeMax": 15, "precision": 10},
            "webgl-extensions": [
                "ANGLE_instanced_arrays",
                "EXT_blend_minmax",
                "EXT_color_buffer_half_float",
                "EXT_disjoint_timer_query",
                "EXT_float_blend",
                "EXT_frag_depth",
                "EXT_shader_texture_lod",
                "EXT_texture_filter_anisotropic",
                "EXT_sRGB",
                "KHR_parallel_shader_compile",
                "OES_element_index_uint",
                "OES_fbo_render_mipmap",
                "OES_standard_derivatives",
                "OES_texture_float",
                "OES_texture_float_linear",
                "OES_texture_half_float",
                "OES_texture_half_float_linear",
                "OES_vertex_array_object",
                "WEBGL_color_buffer_float",
                "WEBGL_compressed_texture_astc",
                "WEBGL_compressed_texture_etc",
                "WEBGL_compressed_texture_etc1",
                "WEBGL_debug_renderer_info",
                "WEBGL_debug_shaders",
                "WEBGL_depth_texture",
                "WEBGL_draw_buffers",
                "WEBGL_lose_context",
                "WEBGL_multi_draw",
                "WEBGL_provoking_vertex",
            ],
            "webgl2-supported": True,
            "webgl2-version": "WebGL 2.0 (OpenGL ES 3.0 Chromium)",
            "webgl2-glsl-version": "WebGL GLSL ES 3.00 (OpenGL ES GLSL ES 3.0 Chromium)",
        })

    def auc(slf):
        ah = hsh.sha1(b"pixel9pro_audio_fingerprint").hexdigest()
        slf.dd.update({
            "ac-base-latency": 0.005333333333333333,
            "ac-output-latency": 0,
            "ac-sample-rate": 48000,
            "ac-state": "running",
            "ac-max-channel-count": 2,
            "ac-number-of-inputs": 1,
            "ac-number-of-outputs": 1,
            "ac-channel-count": 2,
            "ac-channel-count-mode": "explicit",
            "ac-channel-interpretation": "speakers",
            "ac-fft-size": 2048,
            "ac-frequency-bin-count": 1024,
            "ac-min-decibels": -100,
            "ac-max-decibels": -30,
            "ac-smoothing-time-constant": 0.8,
            "ac-print": ah,
            "ac-print-raw": "124.04344884395687",
        })

    def can(slf):
        cb = b"pixel9pro_canvas_fingerprint"
        ch = hsh.sha1(cb).hexdigest()
        cdh = hsh.sha1(cb + b"_detailed").hexdigest()
        slf.dd.update({
            "canvas-print-100-999": ch,
            "canvas-print-detailed-100-999": cdh,
            "canvas_spoofing": 0,
        })

    def tim(slf):
        nw = dtt.now()
        uts = int(tme.time() * 1000)
        toff = -480
        slf.dd.update({
            "time-unix-epoch-ms": uts,
            "time-local": nw.strftime("%m/%d/%Y, %I:%M:%S %p"),
            "time-string": nw.strftime("%a %b %d %Y %H:%M:%S GMT-0800 (Pacific Standard Time)"),
            "time-tz-offset-minutes": toff,
            "time-tz-has-dst": "true",
            "time-tz-dst-active": "false",
            "time-tz-std-offset": toff,
            "time-tz-fixed-locale-string": "3/6/2014, 7:58:39 AM",
        })

    def con(slf):
        slf.dd.update({
            "navigator.connection.effectiveType": "4g",
            "navigator.connection.rtt": 50,
            "navigator.connection.saveData": False,
        })

    def bat(slf):
        slf.dd.update({
            "navigator.battery.level": str(rnd.uniform(0.5, 1.0)),
            "navigator.battery.charging": str(rnd.choice([True, False])).lower(),
            "navigator.battery.chargingTime": "Infinity",
            "navigator.battery.dischargingTime": str(rnd.randint(10000, 50000)),
        })

    def bfe(slf):
        slf.dd.update({
            "browser-features": {
                "css_reflections_support": False,
                "css_scrollbar_support": True,
                "custom_protocol_handler_support": True,
                "effective_type": True,
                "filesystem_support": True,
                "font_display_support": True,
                "input_search_event_support": True,
                "input_types_month_support": True,
                "input_types_week_support": True,
                "prefetch_support": True,
                "quota_management_support": True,
                "speech_recognition_support": True,
                "todataurl_webp_support": True,
                "vibrate_support": True,
                "video_hls": False,
                "web_sql_database_support": True,
                "hairline": True,
            },
            "ex_browser_type": "Chrome Webkit",
        })

    def css(slf):
        slf.dd.update({
            "css-flags": {
                "pointer-type": "coarse",
                "screen-interface": "touch",
                "color-scheme": "light",
                "reduced-motion": False,
                "display-flex": True,
                "display-grid": True,
            },
        })

    def stg(slf):
        tg = slf.tg()
        cookie_tag = quote(tg, safe="")
        slf.dd.update({
            "_t": CCJS_TOKEN,
            "cookie-_cc": cookie_tag,
            "cookie-_cid_cc": cookie_tag,
            "dom-local-tag": tg,
            "cid-dom-local-tag": tg,
            "dom-session-tag": tg,
            "cid-dom-session-tag": tg,
            "fresh-cookie": "true",
            "cf_flags": "1022963",
            "ccjs_version": "IIHGun4MNYWxXjVZRxge8w==",
        })

    def misc(slf):
        slf.dd.update({
            "private-browser": {"browser": "Chrome", "enabled": False},
            "navigator.storage.persisted": False,
            "document.storage.access": False,
            "granted-permissions": {
                "accelerometer": "granted",
                "gyroscope": "granted",
                "magnetometer": "granted",
                "geolocation": "prompt",
                "camera": "prompt",
                "microphone": "prompt",
                "notifications": "prompt",
            },
            "mobile-device-motion": {
                "acceleration": {"x": "0.000", "y": "0.000", "z": "0.000"},
                "acceleration.including.gravity": {"x": "0.000", "y": "9.800", "z": "0.000"},
                "rotation": {"alpha": "0.000", "beta": "0.000", "gamma": "0.000"},
            },
            "mobile-device-orientation": {
                "absolute": False,
                "alpha": 0,
                "beta": 0,
                "gamma": 0,
            },
            "webgl_noise_detect": 0,
            "emjh": hsh.sha256(b"pixel9pro_emoji").hexdigest(),
            "flash-installed": "false",
            "flash-enabled": "false",
            "media-capabilities": {
                "video-decode-h264": {"supported": True, "smooth": True, "powerEfficient": True},
                "video-decode-h265": {"supported": True, "smooth": True, "powerEfficient": True},
                "video-decode-vp8": {"supported": True, "smooth": True, "powerEfficient": True},
                "video-decode-vp9": {"supported": True, "smooth": True, "powerEfficient": True},
                "video-decode-av1": {"supported": True, "smooth": True, "powerEfficient": True},
                "audio-decode-aac": {"supported": True, "smooth": True, "powerEfficient": True},
                "audio-decode-opus": {"supported": True, "smooth": True, "powerEfficient": True},
            },
            "timing-sync-collection": rnd.randint(45, 85),
            "timing-total-collection": rnd.randint(180, 320),
            "script-load-time": int(tme.time() * 1000) - rnd.randint(500, 2000),
            "device-data-captured-time": int(tme.time() * 1000),
            "performance-now-precision": 0.1,
            "date-now-offset": rnd.randint(-2, 2),
            "drm-widevine-supported": True,
            "drm-widevine-level": "L1",
            "hdr-support": True,
            "hdr10-plus": True,
            "dolby-vision": False,
        })

    def tg(slf) -> str:
        return CCJS_TAG

    def get_device_data(slf) -> dict:
        return slf.dd.copy()

    def get_encoded_payload(slf) -> str:
        st = jsn.dumps(slf.dd, separators=(",", ":"))
        return xor_base64_utf8(st)

    def get_headers(slf) -> dict:
        ver = "131.0.6778.135"
        return {
            "User-Agent": f"Mozilla/5.0 (Linux; Android 15; Pixel 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver} Mobile Safari/537.36",
            "Sec-Ch-Ua": '"Chromium";v="131", "Google Chrome";v="131", "Not_A Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?1",
            "Sec-Ch-Ua-Platform": '"Android"',
            "Sec-Ch-Ua-Platform-Version": '"15.0.0"',
            "Sec-Ch-Ua-Model": '"Pixel 9 Pro"',
            "Sec-Ch-Ua-Full-Version": ver,
            "Sec-Ch-Ua-Arch": '"arm"',
            "Sec-Ch-Ua-Bitness": '"64"',
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

    def update_timestamps(slf):
        slf.tim()
        slf.bat()

def create_pixel9pro_fingerprint() -> dict:
    px = Pixel9ProSpoof()
    return px.get_device_data()

def get_pixel9pro_headers() -> dict:
    px = Pixel9ProSpoof()
    return px.get_headers()

# ======================================================================
# engine/utils.py
# ======================================================================

from curl_cffi import requests, CurlHttpVersion
import requests as req
from typing import Optional, Dict, List
import json
import random
import asyncio


class RequestHandler:
    def __init__(self, config: Dict = None, assigned_proxy: str = None):
        self.session = requests.Session()
        self.proxies_enabled = False
        self.current_proxy = None

        if config:
            self.proxies_enabled = config.get('proxies_enabled', False)
            if self.proxies_enabled and assigned_proxy:
                self.current_proxy = assigned_proxy
                self.session.proxies = {
                    'http': assigned_proxy,
                    'https': assigned_proxy
                }
                print(f'[✓] Using assigned proxy: {assigned_proxy[:20]}...')
            elif self.proxies_enabled and not assigned_proxy:
                print('[!] Proxies enabled but no proxy assigned')
                self.proxies_enabled = False
    
    @staticmethod
    def load_proxies() -> List[str]:
        try:
            with open('proxies.txt', 'r') as f:
                lines = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

            proxies = []
            for line in lines:
                proxy = RequestHandler._parse_proxy_static(line)
                if proxy:
                    proxies.append(proxy)

            return proxies
        except FileNotFoundError:
            print('[!] proxies.txt not found')
            return []
        except Exception as e:
            print(f'[!] Error loading proxies: {e}')
            return []

    @staticmethod
    def remove_proxy_from_file(proxy_to_remove: str):
        try:
            with open('proxies.txt', 'r') as f:
                lines = f.readlines()

            # Filter out the proxy that was used
            remaining_lines = []
            for line in lines:
                if line.strip() and not line.strip().startswith('#'):
                    parsed = RequestHandler._parse_proxy_static(line.strip())
                    if parsed != proxy_to_remove:
                        remaining_lines.append(line)
                else:
                    remaining_lines.append(line)

            with open('proxies.txt', 'w') as f:
                f.writelines(remaining_lines)

            print(f'[✓] Removed proxy from proxies.txt')
        except Exception as e:
            print(f'[!] Error removing proxy from file: {e}')
    
    @staticmethod
    def _parse_proxy_static(proxy_string: str) -> Optional[str]:
        """Format proxies - handles various formats"""
        # Handle proxies that already have http:// or https:// prefix
        if proxy_string.startswith('http://') or proxy_string.startswith('https://'):
            protocol = 'https://' if proxy_string.startswith('https://') else 'http://'
            remaining = proxy_string[len(protocol):]

            if '@' in remaining:
                return proxy_string

            parts = remaining.split(':')

            if len(parts) == 2:
                return proxy_string

            elif len(parts) == 4:
                host, port, user, password = parts
                return f'{protocol}{user}:{password}@{host}:{port}'

            else:
                print(f'[!] Could not parse proxy format with protocol: {proxy_string}')
                return None

        if '@' in proxy_string:
            auth, location = proxy_string.split('@', 1)
            return f'http://{auth}@{location}'

        parts = proxy_string.split(':')

        if len(parts) == 2:
            ip, port = parts
            return f'http://{ip}:{port}'

        elif len(parts) == 4:
            first_looks_like_ip = '.' in parts[0] or parts[0].replace('.', '').isdigit()

            if first_looks_like_ip:
                ip, port, user, password = parts
                return f'http://{user}:{password}@{ip}:{port}'
            else:
                user, password, ip, port = parts
                return f'http://{user}:{password}@{ip}:{port}'

        print(f'[!] Could not parse proxy format: {proxy_string}')
        return None

    def reset_session(self):
        self.session.close()
        self.session = requests.Session()
        if self.proxies_enabled and self.current_proxy:
            self.session.proxies = {
                'http': self.current_proxy,
                'https': self.current_proxy
            }

    async def _get_ip_info(self):
        response = await self.get("Get Proxy Information", "http://ip-api.com/json/")
        if response:
            return response.json()
        return None

    async def get(self, name: str, url: str, headers: Dict=None, params: Dict=None) -> Optional[requests.Response]:
        try:
            try:
                response = self.session.get(
                    url,
                    headers=headers,
                    params=params,
                    timeout=10,
                    impersonate='chrome116',
                    )
            except:
                print("Trying http1...")
                response = self.session.get(
                    url,
                    headers=headers,
                    params=params,
                    timeout=30,
                    impersonate='chrome116',
                    http_version=CurlHttpVersion.V1_1,
                    )

            if response.status_code == 200:
                print(f'[✓] {name} request successful')
                return response
            else:
                print(f'[✗] {name} failed: {response.status_code}')
                print(f'    Response: {response.text[:200]}...')
                return None

        except Exception as e:
            print(f"[!] Request error in {name}: {e}")
            return None

    async def post(self, name: str, url: str, headers: Dict, data: Dict) -> Optional[requests.Response]:
        try:
            # try curl cffi default request, if fails then switch to http1. some proxies dont support higher level http hence this block
            try:
                response = self.session.post(
                    url,
                    headers=headers,
                    data=json.dumps(data, separators=(",", ":")),
                    timeout=10,
                    impersonate='chrome116',
                )
            except:
                print("Trying http1...")
                response = self.session.post(
                    url,
                    headers=headers,
                    data=json.dumps(data, separators=(",", ":")),
                    timeout=30,
                    impersonate='chrome116',
                    http_version=CurlHttpVersion.V1_1,
                )

            if response.status_code == 200 or (response.status_code == 204 and name == 'Get UDI Fingerprint'):
                print(f'[✓] {name} request successful')
                return response
            else:
                print(f'[✗] {name} failed: {response.status_code}')
                print(f'    Response: {response.text[:200]}...')
                return None

        except Exception as e:
            print(f"[!] Request error in {name}: {e}")
            return None
        

# ======================================================================
# device.py
# ======================================================================

import os
import json
import uuid
import time
import hashlib
from typing import Dict, Tuple
import random
from curl_cffi import requests

import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
import secrets


def base64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('ascii')


class DeviceProfile:
    def __init__(self, request_handler: RequestHandler = None):
        self.read_config()
        self.request_handler = request_handler if request_handler else RequestHandler()
        self.phone_type_flow = self.config['phone_type_flow']

        # App specifics
        self.first_party_client_id = 'S_Fwp1YMY1qAlAf5-yfYbeb7cfJE-50z'
        if self.config['app_variant'] == 'postmates':
            self.version = '6.299.10001'
            self.client_id = 'com.postmates.android'
            self.app_variant = 'postmates'
            self.app_url = f'uberlogin://auth3.uber.com/applogin/postmates'
            self.version_checksum = '50bd155c2f4fd6a9d6031196a40b80a0'
        elif self.config['app_variant'] == 'ubereats':
            self.version = '6.309.10001'
            self.client_id = 'com.ubercab.UberEats' if self.phone_type_flow == 'iphone' else 'com.ubercab.eats'
            self.app_variant = 'ubereats'
            self.app_url = f'uberlogin://auth3.uber.com/applogin/eats'
            self.version_checksum = 'cfba4a2d6551b6ef719f44d7f8d4a880'
        else:
            raise ValueError(f"Invalid app variant: {self.config['app_variant']}")

        # Device Specifics
        if self.phone_type_flow == 'iphone':
            self.device_type = 'iphone'
            self.manufacturer = 'Apple'
            self.user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
            self.cronet_ua = self.user_agent
            self.os = '18.3.2'
            self.sdk = ''
            self.brand = 'Apple'
            self.model = 'iPhone17,3'
            self.phone_name = 'iPhone 16'
            self.device_width = 1179
            self.device_height = 2556
            self.cpu_abi = '16777228-2'
        else:
            self.device_type = 'android'
            self.manufacturer = 'Google'
            self.user_agent = self.device_json['user_agent']
            self.cronet_ua = 'Cronet/129.0.6668.102@aa3a5623'
            self.os = self.device_json['os_latest']
            self.sdk = '35'
            self.brand = self.device_json['brand']
            self.model = self.device_json['model']
            self.phone_name = self.device_json['phone_name']
            self.device_width = self.device_json['width']
            self.device_height = self.device_json['height']
            self.cpu_abi = self.device_json['cpuAbi']

        self.location_city = None  # Will be set in initialize
        self.location_country = 'US'
        self.latitude = None  # Will be set in initialize
        self.longitude = None  # Will be set in initialize

        self.udid = str(uuid.uuid4())
        self.app_device_id = str(uuid.uuid4())
        self.cold_launch_id = str(uuid.uuid4())
        self.hot_launch_id = str(uuid.uuid4())
        self.client_user_analytics_session_id = str(uuid.uuid4())
        self.call_uuid = str(uuid.uuid4())
        self.client_network_request_uuid = str(uuid.uuid4())
        self.client_session_uuid = str(uuid.uuid4())

        self.android_id = secrets.token_hex(8)
        self.android_id_uuid = str(uuid.uuid4())
        self.google_advertising_id = str(uuid.uuid4())
        self.google_app_set_id = str(uuid.uuid4())
        self.installation_uuid = str(uuid.uuid4())
        self.drm_id = secrets.token_hex(32).upper()
        self.device_id = hashlib.md5(self.android_id.encode()).hexdigest()


        self.ip_address = f"192.168.1.{random.randint(1, 254)}"
        self.device_epoch = int(time.time() * 1000)
        self.pkce_verifier, self.pkce_challenge = self._generate_pkce()
        self.trace_id = self._generate_trace_id()

    async def initialize(self):
        ip_info = await self.request_handler._get_ip_info()
        if ip_info:
            self.location_city = ip_info.get('timezone', 'America/Los_Angeles')
            self.latitude = str(ip_info.get('lat', 0.0))
            self.longitude = str(ip_info.get('lon', 0.0))
            print(f'[✓] Device location set: {self.location_city} ({self.latitude}, {self.longitude})')
        else:
            # Fallback values if IP info fails
            self.location_city = 'America/Los_Angeles'
            self.latitude = '0.0'
            self.longitude = '0.0'
            print(f'[!] Failed to get IP info, using fallback location')

    def read_config(self):
        with open("config.json", "r") as f:
            self.config = json.load(f)
        with open("devices.json", "r") as f:
            tem = json.load(f)
            self.device_json = random.choice(tem['devices'])

    def generate_uber_session(self, session_id: str, session_duration_ms: int = 1800000) -> str:
        now_ms = int(time.time() * 1000)

        inner_session = {
            "session_id": {
                "uuid": {
                    "value": session_id
                }
            },
            "expires_at": {"value": now_ms + session_duration_ms},
            "created_at": {"value": now_ms}
        }

        inner_b64 = base64.b64encode(
            json.dumps(inner_session, separators=(',', ':')).encode()
        ).decode()

        user_session_b64 = base64.b64encode(inner_b64.encode()).decode()

        outer_session = {
            "user_session": user_session_b64,
            "cookie_expires_at": {"value": now_ms + 10000},  # +10 sec
            "cookie_created_at": {"value": now_ms},
            "action": 2
        }

        tem = base64.b64encode(
            json.dumps(outer_session, separators=(',', ':')).encode()
        ).decode()
        tem = tem[:-2]
        return tem

    def _generate_pkce(self) -> Tuple[str, str]:
        verifier = base64url(os.urandom(32))
        while len(verifier) != 43:
            verifier = base64url(os.urandom(32))
        challenge = base64url(hashlib.sha256(verifier.encode()).digest())
        return verifier, challenge

    def _generate_perf_id(self) -> str:
        install_uuid = self.installation_uuid.replace('-', '')
        timestamp_seconds = int(time.time())
        combined = f"{install_uuid}{timestamp_seconds}{self.android_id}"
        sha1_hash = hashlib.sha1(combined.encode()).hexdigest()[:32]
        return f"{sha1_hash[0:8]}-{sha1_hash[8:12]}-{sha1_hash[12:16]}-{sha1_hash[16:20]}-{sha1_hash[20:32]}".upper()
    
    def _generate_trace_id(self) -> str:
        trace_id = secrets.token_hex(16)
        span_id = secrets.token_hex(8)
        parent_span_id = "0"
        flags = "0"

        return f"{trace_id}:{span_id}:{parent_span_id}:{flags}"

    def _generate_epoch(self) -> float:
        return time.time() * 1000

    def build_device_data_v2(self) -> str:
        epoch_ms = int(self._generate_epoch())
        session_start_ms = epoch_ms - random.randint(1000, 5000)
        foreground_start_ms = session_start_ms + random.randint(500, 2000)
        
        data = {
            "data": {
                "dimensions": {
                    "android_id": self.android_id,
                    "drm_id": self.drm_id,
                    "google_advertising_id": self.google_advertising_id,
                    "ip_address": self.ip_address,
                    "is_emulator": False,
                    "perf_id": self._generate_perf_id()
                },
                "name": "device_data_collection"
            },
            "meta": {
                "app": {
                    "app_variant": self.app_variant,
                    "build_type": "release",
                    "build_uuid": str(uuid.uuid4()),
                    "commit_hash": secrets.token_hex(20),
                    "id": self.client_id,
                    "type": "eats_app",
                    "version": self.version
                },
                "carrier": {
                    "mcc": "310",
                    "mnc": "260",
                    "name": "T-Mobile"
                },
                "device": {
                    "app_device_uuid": self.app_device_id,
                    "battery_level": round(random.uniform(0.5, 1.0), 1),
                    "battery_status": "unplugged",
                    "cpu_abi": ", arm64-v8a",
                    "device_id": self.device_id,
                    "drm_id": self.drm_id,
                    "google_advertising_id": self.google_advertising_id,
                    "google_play_services_status": "success",
                    "google_play_services_version": "25.47.30 (190400-833691957)",
                    "installation_id": self.installation_uuid,
                    "ip_address": self.ip_address,
                    "language": "en",
                    "locale": "en_US",
                    "manufacturer": "Google",
                    "model": self.model.lower(),
                    "os_arch": "aarch64",
                    "os_type": "android",
                    "os_version": self.os,
                    "os_version_build": "UE1A.230829.036.A4",
                    "screen_density": 3.2,
                    "screen_height_pixels": int(self.device_height),
                    "screen_width_pixels": int(self.device_width),
                    "thermal_state": "nominal",
                    "year_class": 2014
                },
                "network": {
                    "latency_band": "SLOW",
                    "type": "Unknown"
                },
                "session": {
                    "app_lifecycle_state": "foreground",
                    "cold_launch_id": self.cold_launch_id,
                    "foreground_start_time_ms": foreground_start_ms,
                    "hot_launch_id": self.hot_launch_id,
                    "session_id": self.client_session_uuid,
                    "session_start_time_ms": session_start_ms
                }
            }
        }
        
        return json.dumps(data)

    def build_device_data(self) -> str:
        BATTERY_STATUSES = ['unplugged']
        epoch = self._generate_epoch()

        if self.phone_type_flow == 'iphone':
            device_data = {
                "deviceOsVersion": "18.3.2",
                "carrierMnc": "65535",
                "envChecksum": "1fa5c4fb68087c3d86a7e3d76c6591ea",
                "deviceIds": {
                    "advertiserId": "00000000-0000-0000-0000-000000000000",
                    "uberId": self.udid.upper(),
                    "perfId": self._generate_perf_id().upper(),
                    "vendorId": self.app_device_id.upper(),
                },
                "wifiConnected": True,
                "version": self.version,
                "libCount": 1123,
                "locationServiceEnabled": False,
                "deviceModel": "iPhone17,3",
                "carrierMcc": "65535",
                "versionChecksum": self.version_checksum,
                "carrier": "--",
                "deviceName": "iPhone",
                "rooted": False,
                "envId": "454750e9f0a8953573da55b1aef89a1d",
                "sourceApp": "eats",
                "batteryLevel": 1,
                "batteryStatus": random.choice(BATTERY_STATUSES),
                "epoch": epoch,
                "deviceOsName": "iOS",
                "cpuAbi": "16777228-2",
                "ipAddress": self.ip_address,
            }

            raw_json = json.dumps(device_data, separators=(",", ":"))
            raw_json = json.dumps(raw_json)
            return raw_json

        epoch_sci = f"{epoch:.12E}".replace("+", "")

        device_data = {
            "androidId": self.android_id,
            "batteryLevel": round(random.uniform(0.1, 1.0), 2),
            "batteryStatus": random.choice(BATTERY_STATUSES),
            "carrier": "",
            "carrierMcc": "",
            "carrierMnc": "",
            "course": 0.0,
            "cpuAbi": ", arm64-v8a, armeabi, armeabi-v7a",
            "deviceAltitude": 0.0,
            "deviceIds": {
                "androidId": self.android_id,
                "appDeviceId": self.app_device_id,
                "drmId": self.drm_id,
                "googleAdvertisingId": self.google_advertising_id,
                "googleAppSetId": self.google_app_set_id,
                "installationUuid": self.installation_uuid,
                "perfId": self._generate_perf_id(),
                "udid": self.udid,
                "unknownItems": {"a": []},
            },
            "deviceLatitude": float(self.latitude),
            "deviceLongitude": float(self.longitude),
            "deviceModel": self.model,
            "deviceOsName": "Android",
            "deviceOsVersion": self.os,
            "emulator": False,
            "epoch": {"value": "__EPOCH_PLACEHOLDER__"},
            "horizontalAccuracy": 0.0,
            "ipAddress": self.ip_address,
            "libCount": 0,
            "locationServiceEnabled": False,
            "mockGpsOn": False,
            "rooted": False,
            "sourceApp": "eats",
            "specVersion": "2.0",
            "speed": 0.0,
            "systemTimeZone": self.location_city,
            "unknownItems": {"a": []},
            "version": self.version,
            "versionChecksum": self.version_checksum,
            "verticalAccuracy": 0.0,
            "wifiConnected": True,
        }

        raw_json = json.dumps(device_data, separators=(",", ":"))
        raw_json = raw_json.replace('"__EPOCH_PLACEHOLDER__"', epoch_sci)
        raw_json = json.dumps(raw_json)
        return raw_json

    def build_usl_url(self) -> str:
        from urllib.parse import quote

        params = {
            "showDebugInfo": "false",
            "x-uber-device": self.device_type,
            "x-uber-client-name": "eats",
            "x-uber-client-version": self.version,
            "x-uber-client-id": self.client_id,
            "firstPartyClientID": self.first_party_client_id,
            "isEmbedded": "true",
            "codeChallenge": self.pkce_challenge,
            "app_url": f"https://auth3.uber.com/applogin/{self.app_variant}",
            "asms": "true",
            "x-uber-device-udid": self.udid,
            "sim_mcc": "",
            "sim_mnc": "",
            "x-uber-app-device-id": self.app_device_id,
            "x-uber-device-location-latitude": self.latitude,
            "x-uber-device-location-longitude": self.longitude,
            "socialNative": "g",
            "x-uber-cold-launch-id": self.cold_launch_id,
            "x-uber-hot-launch-id": self.hot_launch_id,
            "x-uber-app-variant": self.app_variant,
            "countryCode": "",
            "known_user": "false",
            "isChromeCustomTabSession": "false",
        }

        items = []
        for k, v in params.items():
            if k == "app_url":
                items.append(f"{k}={quote(v, safe='')}")
            else:
                items.append(f"{k}={v}")

        return "https://auth.uber.com/v2?" + "&".join(items)

    def build_cit_token(self) -> str:
        # first /rt/devices/task request. not sure if this is relevant. doing this request possible for backend to initialize?
        # need to do more research. /rt/devices/results is the one that gives the cit token.

        headers = {
            'x-uber-device-mobile-iso2': 'US',
            'x-uber-drm-id': self.drm_id,
            'x-uber-device': self.device_type,
            'x-uber-device-language': 'en_US',
            'user-agent': self.cronet_ua,
            'x-uber-device-os': self.os,
            'x-uber-device-sdk': self.sdk,
            'x-uber-request-uuid': str(uuid.uuid4()),
            'x-uber-client-user-session-id': self.client_user_analytics_session_id,
            'x-uber-client-version': self.version,
            'x-uber-device-manufacturer': self.manufacturer,
            'x-uber-call-uuid': self.call_uuid,
            'x-uber-device-id': self.device_id,
            'x-uber-markup-textformat-version': '1',
            'x-uber-device-model': self.model,
            'uberctx-mobile-initiated': 'true',
            'x-uber-app-variant': self.app_variant,
            'x-uber-analytics-session-id': self.client_user_analytics_session_id,
            'content-type': 'application/json; charset=UTF-8',
            'uberctx-client-network-request-uuid': self.client_network_request_uuid,
            'x-uber-device-epoch': str(int(self._generate_epoch())),
            'uberctx-cold-launch-id': self.cold_launch_id,
            'x-uber-client-id': self.client_id,
            'x-uber-app-lifecycle-state': 'foreground',
            'x-uber-protocol-version': '0.73.0',
            'x-uber-device-timezone': self.location_city,
            'x-uber-client-name': 'eats',
            'x-uber-client-session': self.client_session_uuid,
            'x-uber-device-time-24-format-enabled': '0',
            'x-uber-app-device-id': self.app_device_id,
            'x-uber-device-voiceover': '0',
            'priority': 'u=1, i',
        }

        json_data = {
            'request': {
                'installationID': self.installation_uuid,
                'clientType': self.device_type,
                'clientIntegrityToken': '',
            },
        }
        json_data = json.dumps(json_data)

        response = requests.post('https://cn-geo1.uber.com/rt/devices/task', headers=headers, data=json_data)

        headers = {
            'x-uber-device-mobile-iso2': 'US',
            'x-uber-drm-id': self.drm_id,
            'x-uber-device': self.device_type,
            'x-uber-device-language': 'en_US',
            'user-agent': self.cronet_ua,
            'x-uber-device-os': self.os,
            'x-uber-device-sdk': self.sdk,
            'x-uber-request-uuid': str(uuid.uuid4()),
            'x-uber-client-user-session-id': self.client_user_analytics_session_id,
            'x-uber-client-version': self.version,
            'x-uber-device-manufacturer': self.manufacturer,
            'x-uber-call-uuid': self.call_uuid,
            'x-uber-device-id': self.device_id,
            'x-uber-markup-textformat-version': '1',
            'x-uber-device-model': self.model,
            'uberctx-mobile-initiated': 'true',
            'x-uber-app-variant': self.app_variant,
            'x-uber-analytics-session-id': self.client_user_analytics_session_id,
            'content-type': 'application/json; charset=UTF-8',
            'x-uber-network-classifier': 'MEDIUM',
            'uberctx-client-network-request-uuid': self.client_network_request_uuid,
            'x-uber-device-epoch': str(int(self._generate_epoch())),
            'uberctx-cold-launch-id': self.cold_launch_id,
            'x-uber-client-id': self.client_id,
            'x-uber-app-lifecycle-state': 'foreground',
            'x-uber-protocol-version': '0.73.0',
            'x-uber-device-timezone': self.location_city,
            'x-uber-client-name': 'eats',
            'x-uber-client-session': self.client_session_uuid,
            'x-uber-device-time-24-format-enabled': '0',
            'x-uber-app-device-id': self.app_device_id,
            'x-uber-device-voiceover': '0',
            'priority': 'u=1, i',
        }

        json_data = {
            'request': {
                'installationID': self.installation_uuid,
                'keyAttestation': {
                    'certificate': '',
                },
                'attemptNumber': 1,
            },
        }
        json_data = json.dumps(json_data)

        response = requests.post('https://cn-geo1.uber.com/rt/devices/results', headers=headers, data=json_data)
        result = response.json()
        if result['status'] != 'UPSERT_STATUS_COMPLETE':
            print('Failed to generate CIT')
            print(response.json())
            print(response.status_code)
            return None

        print('Successfully got CIT Token')
        return result.get('clientIntegrityToken', None)
    
    def build_sig_token(self, headers: dict) -> str:
        private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())

        sig_headers = {}
        for k, v in headers.items():
            k_lower = k.lower()
            if k_lower in ('x-uber-id', 'x-uber-cit'):
                continue
            if k_lower.startswith('x-uber-') or k_lower == 'authorization':
                sig_headers[k_lower] = v

        sorted_keys = sorted(sig_headers.keys())
        header_lines = "\n".join(f"{k}: {sig_headers[k]}" for k in sorted_keys)
        header_names = ";".join(sorted_keys)

        parts = ["a=ES256;v=1", 'POST', '/rt/silk-screen/submit-form', '']
        if header_lines:
            parts.append(header_lines)
        if header_names:
            parts.append(header_names)
        canonical = "\n".join(parts)

        signature = private_key.sign(canonical.encode('utf-8'), ec.ECDSA(hashes.SHA256()))

        return base64.b64encode(signature).decode()

    def generate_msm_attestation_token(self):
        header = {"alg": "ES256", "typ": "JWT"}
        header_b64 = base64.urlsafe_b64encode(json.dumps(header, separators=(',', ':')).encode()).rstrip(b'=').decode()
        
        payload = {
            "requestDetails": {
                "requestPackageName": "com.ubercab.eats",
                "timestampMillis": str(int(time.time() * 1000)),
                "nonce": base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b'=').decode()
            },
            "appIntegrity": {
                "appRecognitionVerdict": "PLAY_RECOGNIZED",
                "packageName": "com.ubercab.eats",
                "certificateSha256Digest": [base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b'=').decode()],
                "versionCode": "1"
            },
            "deviceIntegrity": {"deviceRecognitionVerdict": ["MEETS_DEVICE_INTEGRITY"]},
            "accountDetails": {"appLicensingVerdict": "LICENSED"}
        }
        payload_b64 = base64.urlsafe_b64encode(json.dumps(payload, separators=(',', ':')).encode()).rstrip(b'=').decode()
        signature = base64.urlsafe_b64encode(secrets.token_bytes(64)).rstrip(b'=').decode()
        
        return f"{header_b64}.{payload_b64}.{signature}"

    def get_device_fingerprint(self):
        spoof = Pixel9ProSpoof()
        return spoof.get_encoded_payload()

    def _generate_fingerprint_data(self):
        version = "131.0.6778.135"
        android_version = "15"

        now = datetime.now()
        unix_time = int(time.time() * 1000)

        audio_hash = hashlib.sha1(b"pixel9pro_audio_fingerprint").hexdigest()
        canvas_hash = hashlib.sha1(b"pixel9pro_canvas_fingerprint").hexdigest()
        canvas_detailed = hashlib.sha1(b"pixel9pro_canvas_fingerprint_detailed").hexdigest()
        emoji_hash = hashlib.sha256(b"pixel9pro_emoji").hexdigest()
        tag = self._generate_tag()
        cookie_tag = quote(tag, safe="")

        data = {
            "navigator.appVersion": f"5.0 (Linux; Android {android_version}; Pixel 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Mobile Safari/537.36",
            "navigator.appName": "Netscape",
            "navigator.product": "Gecko",
            "navigator.platform": "Linux armv8l",
            "navigator.language": "en-US",
            "navigator.userAgent": f"Mozilla/5.0 (Linux; Android {android_version}; Pixel 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Mobile Safari/537.36",
            "navigator.cookieEnabled": True,
            "navigator.hardwareConcurrency": 8,
            "navigator.deviceMemory": 8,
            "navigator.doNotTrack": "null",
            "navigator.automationEnabled": False,
            "navigator.maxTouchPoints": 5,
            "touchEnabled": True,
            "webdriver_detect": False,
            "navigator.vendor": "Google Inc.",
            "navigator.productSub": "20030107",
            "navigator.appCodeName": "Mozilla",
            "window.screen.colorDepth": "24",
            "window.screen.pixelDepth": "24",
            "window.screen.height": "2992",
            "window.screen.width": "1344",
            "window.screen.availHeight": "2847",
            "screen.availWidth": "1344",
            "screen.availHeight": "2847",
            "window.devicePixelRatio": "3",
            "window.screen.orientation.type": "portrait-primary",
            "window.screen.orientation.angle": "0",
            "window.screen.darkMode.enabled": False,
            "window.outerWidth": "448",
            "window.outerHeight": "949",
            "window.innerWidth": "448",
            "window.innerHeight": "865",
            "window.history.length": str(random.randint(1, 10)),
            "window.clientInformation.language": "en-US",
            "window.doNotTrack": "null",
            "navigator.userAgentData.brands": [
                {"brand": "Chromium", "version": "131"},
                {"brand": "Google Chrome", "version": "131"},
                {"brand": "Not_A Brand", "version": "24"}
            ],
            "navigator.userAgentData.mobile": True,
            "navigator.userAgentData.platform": "Android",
            "navigator.userAgentData.highEntropyValues.platform": "Android",
            "navigator.userAgentData.highEntropyValues.platformVersion": "15.0.0",
            "navigator.userAgentData.highEntropyValues.architecture": "arm",
            "navigator.userAgentData.highEntropyValues.bitness": "64",
            "navigator.userAgentData.highEntropyValues.model": "Pixel 9 Pro",
            "navigator.userAgentData.highEntropyValues.uaFullVersion": version,
            "navigator.userAgentData.highEntropyValues.fullVersionList": [
                {"brand": "Chromium", "version": version},
                {"brand": "Google Chrome", "version": version},
                {"brand": "Not_A Brand", "version": "24.0.0.0"}
            ],
            "webgl-supported": True,
            "webgl-version": "WebGL 1.0 (OpenGL ES 2.0 Chromium)",
            "webgl-glsl-version": "WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)",
            "webgl-vendor": "WebKit",
            "webgl-renderer": "WebKit WebGL",
            "webgl-vendor-real": "ARM",
            "webgl-renderer-real": "Mali-G715-Immortalis MC11",
            "webgl-max-aa": "16",
            "webgl-unmasked-vendor": "ARM",
            "webgl-unmasked-renderer": "ANGLE (ARM, Mali-G715-Immortalis MC11, OpenGL ES 3.2)",
            "webgl-vertex-shader-highp-float": {"rangeMin": 127, "rangeMax": 127, "precision": 23},
            "webgl-vertex-shader-mediump-float": {"rangeMin": 15, "rangeMax": 15, "precision": 10},
            "webgl-fragment-shader-highp-float": {"rangeMin": 127, "rangeMax": 127, "precision": 23},
            "webgl-fragment-shader-mediump-float": {"rangeMin": 15, "rangeMax": 15, "precision": 10},
            "webgl-extensions": [
                "ANGLE_instanced_arrays", "EXT_blend_minmax", "EXT_color_buffer_half_float",
                "EXT_disjoint_timer_query", "EXT_float_blend", "EXT_frag_depth",
                "EXT_shader_texture_lod", "EXT_texture_filter_anisotropic", "EXT_sRGB",
                "KHR_parallel_shader_compile", "OES_element_index_uint", "OES_fbo_render_mipmap",
                "OES_standard_derivatives", "OES_texture_float", "OES_texture_float_linear",
                "OES_texture_half_float", "OES_texture_half_float_linear", "OES_vertex_array_object",
                "WEBGL_color_buffer_float", "WEBGL_compressed_texture_astc", "WEBGL_compressed_texture_etc",
                "WEBGL_compressed_texture_etc1", "WEBGL_debug_renderer_info", "WEBGL_debug_shaders",
                "WEBGL_depth_texture", "WEBGL_draw_buffers", "WEBGL_lose_context", "WEBGL_multi_draw",
                "WEBGL_provoking_vertex"
            ],
            "webgl2-supported": True,
            "webgl2-version": "WebGL 2.0 (OpenGL ES 3.0 Chromium)",
            "webgl2-glsl-version": "WebGL GLSL ES 3.00 (OpenGL ES GLSL ES 3.0 Chromium)",
            "ac-base-latency": 0.005333333333333333,
            "ac-output-latency": 0,
            "ac-sample-rate": 48000,
            "ac-state": "running",
            "ac-max-channel-count": 2,
            "ac-number-of-inputs": 1,
            "ac-number-of-outputs": 1,
            "ac-channel-count": 2,
            "ac-channel-count-mode": "explicit",
            "ac-channel-interpretation": "speakers",
            "ac-fft-size": 2048,
            "ac-frequency-bin-count": 1024,
            "ac-min-decibels": -100,
            "ac-max-decibels": -30,
            "ac-smoothing-time-constant": 0.8,
            "ac-print": audio_hash,
            "ac-print-raw": "124.04344884395687",
            "canvas-print-100-999": canvas_hash,
            "canvas-print-detailed-100-999": canvas_detailed,
            "canvas_spoofing": 0,
            "time-unix-epoch-ms": unix_time,
            "time-local": now.strftime("%m/%d/%Y, %I:%M:%S %p"),
            "time-string": now.strftime("%a %b %d %Y %H:%M:%S GMT-0800 (Pacific Standard Time)"),
            "time-tz-offset-minutes": -480,
            "time-tz-has-dst": "true",
            "time-tz-dst-active": "false",
            "time-tz-std-offset": -480,
            "time-tz-fixed-locale-string": "3/6/2014, 7:58:39 AM",
            "navigator.connection.effectiveType": "4g",
            "navigator.connection.rtt": 50,
            "navigator.connection.saveData": False,
            "navigator.battery.level": str(round(random.uniform(0.5, 1.0), 2)),
            "navigator.battery.charging": str(random.choice([True, False])).lower(),
            "navigator.battery.chargingTime": "Infinity",
            "navigator.battery.dischargingTime": str(random.randint(10000, 50000)),
            "browser-features": {
                "css_reflections_support": False,
                "css_scrollbar_support": True,
                "custom_protocol_handler_support": True,
                "effective_type": True,
                "filesystem_support": True,
                "font_display_support": True,
                "input_search_event_support": True,
                "input_types_month_support": True,
                "input_types_week_support": True,
                "prefetch_support": True,
                "quota_management_support": True,
                "speech_recognition_support": True,
                "todataurl_webp_support": True,
                "vibrate_support": True,
                "video_hls": False,
                "web_sql_database_support": True,
                "hairline": True,
            },
            "ex_browser_type": "Chrome Webkit",
            "css-flags": {
                "pointer-type": "coarse",
                "screen-interface": "touch",
                "color-scheme": "light",
                "reduced-motion": False,
                "display-flex": True,
                "display-grid": True,
            },
            "_t": CCJS_TOKEN,
            "cookie-_cc": cookie_tag,
            "cookie-_cid_cc": cookie_tag,
            "dom-local-tag": tag,
            "cid-dom-local-tag": tag,
            "dom-session-tag": tag,
            "cid-dom-session-tag": tag,
            "fresh-cookie": "true",
            "cf_flags": "1022963",
            "ccjs_version": "IIHGun4MNYWxXjVZRxge8w==",
            "private-browser": {"browser": "Chrome", "enabled": False},
            "navigator.storage.persisted": False,
            "document.storage.access": False,
            "granted-permissions": {
                "accelerometer": "granted",
                "gyroscope": "granted",
                "magnetometer": "granted",
                "geolocation": "prompt",
                "camera": "prompt",
                "microphone": "prompt",
                "notifications": "prompt",
            },
            "mobile-device-motion": {
                "acceleration": {"x": "0.000", "y": "0.000", "z": "0.000"},
                "acceleration.including.gravity": {"x": "0.000", "y": "9.800", "z": "0.000"},
                "rotation": {"alpha": "0.000", "beta": "0.000", "gamma": "0.000"},
            },
            "mobile-device-orientation": {
                "absolute": False,
                "alpha": 0,
                "beta": 0,
                "gamma": 0,
            },
            "webgl_noise_detect": 0,
            "emjh": emoji_hash,
            "flash-installed": "false",
            "flash-enabled": "false",
            "media-capabilities": {
                "video-decode-h264": {"supported": True, "smooth": True, "powerEfficient": True},
                "video-decode-h265": {"supported": True, "smooth": True, "powerEfficient": True},
                "video-decode-vp8": {"supported": True, "smooth": True, "powerEfficient": True},
                "video-decode-vp9": {"supported": True, "smooth": True, "powerEfficient": True},
                "video-decode-av1": {"supported": True, "smooth": True, "powerEfficient": True},
                "audio-decode-aac": {"supported": True, "smooth": True, "powerEfficient": True},
                "audio-decode-opus": {"supported": True, "smooth": True, "powerEfficient": True},
            },
            "timing-sync-collection": random.randint(45, 85),
            "timing-total-collection": random.randint(180, 320),
            "script-load-time": int(time.time() * 1000) - random.randint(500, 2000),
            "device-data-captured-time": int(time.time() * 1000),
            "performance-now-precision": 0.1,
            "date-now-offset": random.randint(-2, 2),
            "drm-widevine-supported": True,
            "drm-widevine-level": "L1",
            "hdr-support": True,
            "hdr10-plus": True,
            "dolby-vision": False,
        }

        return data

    def _generate_tag(self):
        return CCJS_TAG

    def _encode_payload(self, data):
        json_str = json.dumps(data, separators=(",", ":"))
        return xor_base64_utf8(json_str)

# ======================================================================
# engine/account_manager.py
# ======================================================================

import uuid
import asyncio

class AccountManager:
    def __init__(self, request_handler: RequestHandler, device_manager: DeviceProfile, sid: str, auth_token: str, user_uuid: str):
        self.request_handler = request_handler
        self.device = device_manager
        self.sid = sid
        self.auth_token = auth_token
        self.user_uuid = user_uuid

    async def change_password(self, new_password: str):
        headers = {
            'x-uber-identity-entrypoint': 'uam',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua': '"Chromium";v="142", "Android WebView";v="142", "Not_A Brand";v="99"',
            'x-uber-device-location-longitude': self.device.longitude,
            'sec-ch-ua-mobile': '?1',
            'x-uber-client-name': 'eats',
            'x-uber-marketing-id': str(uuid.uuid4()),
            'x-uber-request-uuid': str(uuid.uuid4()),
            'x-uber-app-device-id': self.device.app_device_id,
            #'x-uber-infrasec': '0b32ff200030061d:____ibR_Q__4T30PU_Z_S___NW__O6_______cd__Ktu__________j_',
            'x-uber-app-variant': self.device.app_variant,
            'content-type': 'application/json',
            #'x-uber-edge-tls-ja3-fingerprint': '5659c10619c455ea477287b12cf3f7e7',
            'x-uber-device-id': self.device.udid,
            'x-uber-device': self.device.device_type,
            'x-csrf-token': 'x',
            'x-uber-device-language': f'en_{self.device.location_country}',
            'x-uber-device-udid': self.device.udid,
            'x-uber-device-model': self.device.model,
            'x-uber-device-os': self.device.os,
            #'x-uber-edge-botdefense': '842a052ee1c4ecc8a1a6051656e35864:0119d74b7888e3371a206e7ed758e31e32aec0b38f3b2182158d3771b2bbae793de902134e5135aa17b45f29f9e9a4c675f4cc9f0a3ac425a7ddc7a23fa7ec61728d57190fab6bfe1a0c5e7e86634d7ccb95a7eb693c326d5e93b3c1:0:get',
            'x-uber-device-location-latitude': '0',
            'x-uber-client-version': self.device.version,
            'x-uber-device-mobile-iso2': self.device.location_country,
            'x-uber-client-session': self.device.client_session_uuid,
            'x-uber-client-id': self.device.client_id,
            #'x-uber-auth-sso-id': '0538fecc-3cf9-464c-96d2-1b44578e4cf3',
            'user-agent': self.device.user_agent,
            'accept': '*/*',
            'origin': 'https://account.uber.com',
            'x-requested-with': self.device.client_id,
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://account.uber.com/workflow?host_theme=light&workflow_next_url=BACK&workflow=PASSWORD',
            'accept-language': f'en-{self.device.location_country},en;q=0.9',
            'priority': 'u=1, i',
        }

        json_data = {
            'currentScreen': 'PASSWORD',
            'workflowId': {
                'value': 'identity_factor.collect_password',
            },
            'sessionId': {
                'uuid': {
                    'value': '',
                },
            },
            'event': {
                'eventType': 'EVENT_TYPE_ENTER_PASSWORD',
                'enterPassword': {
                    'password': new_password,
                    'cookieSid': self.sid
                },
            },
        }

        response = await self.request_handler.post(
            'Change Password',
            'https://account.uber.com/api/passwordWorkflow?localeCode=en',
            headers=headers,
            data=json_data,
        )
        
        if response:
            print(f'[✓] Password changed successfully')
            return response.json()
        else:
            print(f'[✗] Failed to change password')
            return None

    
    async def apply_promo(self, promo_code: str):
        """
        Apply promo to account using web api
        its better to apply using mobile api because thats what this is based on, ill probably add that in the future but its like this for now

        reason for that is because im missing a pre requisite to the mobile api call which results in 401, maybe apply address, upsert device, or the /target-promotion 401 call
        didnt have time to look into that more so i just added this, still works so i didnt feel like changing it
        """
        headers = {
            'user-agent': self.device.user_agent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://www.ubereats.com',
            'referer': 'https://www.ubereats.com',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=1, i',
        }
        # get web cookies
        await self.request_handler.get('Get Cookies home', 'https://www.ubereats.com', headers=headers)
        await self.request_handler.get('Get SID Cookies', 'https://www.ubereats.com/login-redirect/', headers=headers)

        headers['x-csrf-token'] = 'x'
        headers['content-type'] = 'application/json'
        # maybe session id

        # apply promo
        response = await self.request_handler.post('Add Promo', 'https://www.ubereats.com/_p/api/applyPromoV1', headers=headers, data={'code': promo_code})
        await asyncio.sleep(1)
        response = await self.request_handler.post('Get Promos', 'https://www.ubereats.com/_p/api/getSavingsV1', headers=headers, data={'type': 'ACCOUNT'})
        if response:
            try:
                for promo_json in response.json()['data']['promoManagerSections'][0]['promoManagerItems']:
                    self.promotion_name = promo_json['savingItem']['saving']['presentationData']['title']
                    print(f"[✓] Promotion: {self.promotion_name}")
            except:
                print("[!] No promotion found")

# ======================================================================
# otp_hotmail.py
# ======================================================================

import re
import asyncio
from typing import Optional
from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests
import json
import os


class BannedAccountException(Exception):
    # when hotmail acc is banned. todo implementation
    pass


class HotmailClient:
    def __init__(self, account: str, client_key: str):
        self.account = account
        self.client_key = client_key
        self.api_base = "https://gapi.hotmail007.com/v1/mail"
        self.full_account_string = None

    def remove_from_file(self, filepath: str = 'hotmail_accs.txt'):
        try:
            if not os.path.exists(filepath):
                return

            with open(filepath, 'r') as f:
                lines = f.readlines()

            email = self.account.split(':')[0] if ':' in self.account else self.account
            filtered_lines = [line for line in lines if not line.startswith(email)]

            with open(filepath, 'w') as f:
                f.writelines(filtered_lines)

            print(f"[!] Removed banned account from {filepath}")
        except Exception as e:
            print(f"[✗] Failed to remove account from file: {e}")

    def _handle_ban_if_needed(self, data: dict):
        # Check if account is banned/compromised
        if data.get('code') == 1:
            error_msg = data.get('message', '')
            if 'AADSTS70000' in error_msg or 'compromised' in error_msg.lower() or 'invalid_grant' in error_msg:
                print(f"[✗] BANNED ACCOUNT DETECTED: {self.account.split(':')[0]}")
                print(f"[!] Account is flagged as compromised by Microsoft")
                self.remove_from_file()
                raise BannedAccountException(f"Account {self.account.split(':')[0]} is banned/compromised")

    def _fetch_first_mail(self, folder: str) -> Optional[dict]:
        url = f"{self.api_base}/getFirstMail"
        params = {
            'clientKey': self.client_key,
            'account': self.account,
            'folder': folder
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            print(f"[✗] API request failed ({folder}): {response.status_code}")
            print(f"[✗] Response: {response.text[:200]}")
            return None

        data = response.json()
        if data.get('success') and data.get('code') == 0:
            email_data = data.get('data')
            return email_data if email_data else None

        self._handle_ban_if_needed(data)

        if data.get('code') != 0:
            print(f"[✗] API returned error ({folder}): {data}")
        return None

    def _parse_email_ts(self, email_data: dict) -> Optional[float]:
        if not email_data:
            return None

        for k in ('timestamp', 'time', 'Time', 'date', 'Date', 'receivedAt', 'ReceivedAt', 'receiveTime', 'ReceiveTime'):
            v = email_data.get(k)
            if v is None:
                continue
            try:
                # already numeric (epoch seconds or ms)
                if isinstance(v, (int, float)):
                    # treat very large values as ms
                    return (float(v) / 1000.0) if float(v) > 1e12 else float(v)
                if isinstance(v, str) and v.strip().isdigit():
                    num = float(v.strip())
                    return (num / 1000.0) if num > 1e12 else num
            except Exception:
                pass

        for k in ('DateTime', 'datetime', 'DateTimeUtc', 'dateTime', 'received', 'Received', 'receivedDateTime', 'ReceivedDateTime'):
            v = email_data.get(k)
            if not v:
                continue
            try:
                s = str(v).strip().replace('Z', '+00:00')
                dt = datetime.fromisoformat(s)
                return dt.timestamp()
            except Exception:
                pass

        return None

    def get_latest_email(self, folder: str = 'both') -> Optional[dict]:
        """
        folder:
          - 'inbox' -> only inbox
          - 'junkemail' -> only junk
          - 'both' -> fetch both and return whichever is newest (best-effort by timestamp)
        """
        try:
            folder = (folder or 'both').lower()

            if folder in ('inbox', 'junkemail'):
                return self._fetch_first_mail(folder)

            # default: check BOTH
            inbox_email = self._fetch_first_mail('inbox')
            junk_email = self._fetch_first_mail('junkemail')

            if not inbox_email and not junk_email:
                return None
            if inbox_email and not junk_email:
                return inbox_email
            if junk_email and not inbox_email:
                return junk_email

            inbox_ts = self._parse_email_ts(inbox_email)
            junk_ts = self._parse_email_ts(junk_email)

            # pick newest email from timestamp
            if inbox_ts is not None and junk_ts is not None:
                return inbox_email if inbox_ts >= junk_ts else junk_email

            return inbox_email

        except BannedAccountException:
            raise
        except requests.exceptions.Timeout:
            print(f"[!] Request timed out - API is slow, retrying...")
            return None
        except Exception as e:
            print(f"[✗] Failed to fetch email: {e}")
            return None


class UberOTPExtractor:
    OTP_PATTERNS = [
        r'\b\d{4}\b',
        r'verification code[:\s]+(\d{4})',
        r'code[:\s]+(\d{4})',
        r'>\s*(\d{4})\s*<'
    ]

    def extract(self, html_content: str) -> Optional[str]:
        try:
            soup = BeautifulSoup(html_content, 'html.parser')

            otp_element = soup.find('td', class_='p1b')
            if otp_element:
                text = otp_element.get_text(strip=True)
                if text.isdigit() and len(text) == 4:
                    return text

            otp_element = soup.find('td', class_='p2b')
            if otp_element:
                text = otp_element.get_text(strip=True)
                if text.isdigit() and len(text) == 4:
                    return text

            verification_elements = soup.find_all(string=re.compile(r'verification code', re.I))
            for element in verification_elements:
                if element.parent:
                    parent = element.parent
                    for sibling in parent.find_next_siblings():
                        if sibling.name:
                            text = sibling.get_text(strip=True)
                            if text.isdigit() and len(text) == 4:
                                return text

                    if parent.parent:
                        grandparent = parent.parent
                        for sibling in grandparent.find_next_siblings():
                            if sibling.name:
                                digit_elements = sibling.find_all(string=re.compile(r'\b\d{4}\b'))
                                for digit_element in digit_elements:
                                    text = digit_element.strip()
                                    if text.isdigit() and len(text) == 4:
                                        return text

            bold_elements = soup.find_all(['b', 'strong']) + soup.find_all('td', class_=re.compile(r'bold|p1b|p2b'))
            for element in bold_elements:
                text = element.get_text(strip=True)
                if text.isdigit() and len(text) == 4:
                    return text

            white_boxes = soup.find_all('td', style=re.compile(r'background-color:\s*#ffffff', re.I))
            for box in white_boxes:
                text = box.get_text(strip=True)
                if text.isdigit() and len(text) == 4:
                    return text
                for pattern in self.OTP_PATTERNS:
                    match = re.search(pattern, str(box))
                    if match:
                        code = match.group(1) if match.lastindex else match.group(0)
                        if code.isdigit() and len(code) == 4:
                            return code

            text_content = soup.get_text()
            four_digit_numbers = re.findall(r'\b\d{4}\b', text_content)
            for number in four_digit_numbers:
                if number not in ['2024', '2025', '2023', '2022', '1999', '2000', '2026']:
                    return number

            return None
        except Exception as e:
            print(f"[✗] OTP extraction failed: {e}")
            return None


class EmailOTPExtractor:
    def __init__(self):
        self.extractors = {
            'uber': UberOTPExtractor(),
            'default': UberOTPExtractor()
        }

    def get_otp_from_email(
        self,
        email_client: HotmailClient,
        target_email: str,
        service: str = 'uber',
        timeout: int = 15
    ) -> Optional[str]:
        try:
            start_time = datetime.now()
            extractor = self.extractors.get(service, self.extractors['default'])
            attempt = 0

            while (datetime.now() - start_time).seconds < timeout:
                attempt += 1
                if attempt > 1 and attempt % 5 == 0:
                    print(f"[*] Still waiting for OTP... (attempt {attempt})")

                with open('config.json', 'r') as f:
                    _ = json.load(f).get('folder', 'inbox')

                email_data = email_client.get_latest_email('both')

                if email_data:
                    html_content = email_data.get('Html') or email_data.get('html') or email_data.get('content') or ''
                    text_content = email_data.get('Text') or email_data.get('text') or email_data.get('body') or ''
                    subject = email_data.get('subject', '')

                    skip_subjects = [
                        'New app(s) connected to your Microsoft account',
                        'Microsoft account',
                        'Security alert',
                        'Verification code for Microsoft'
                    ]

                    should_skip = any(skip_text.lower() in subject.lower() for skip_text in skip_subjects)

                    if should_skip:
                        print(f"[*] Skipping non-Uber email: {subject[:50]}...")
                        time.sleep(2)
                        continue

                    if attempt == 1 and (html_content or text_content):
                        print(f"[*] Found email with subject: {subject[:50]}...")

                    if html_content:
                        otp = extractor.extract(html_content)
                        if otp:
                            print(f"[✓] Successfully extracted OTP: {otp}")
                            return otp

                    if text_content:
                        for pattern in UberOTPExtractor.OTP_PATTERNS:
                            match = re.search(pattern, text_content)
                            if match:
                                code = match.group(1) if match.lastindex else match.group(0)
                                if code.isdigit() and len(code) == 4:
                                    print(f"[✓] Found OTP in text: {code}")
                                    return code

                wait_time = min(2 + (attempt // 3), 5)
                time.sleep(wait_time)

            print("[!] Timeout waiting for OTP email")
            return None
        except Exception as e:
            print(f"[✗] Error getting OTP: {e}")
            return None

    async def get_otp_async(
        self,
        email_client: HotmailClient,
        target_email: str,
        service: str = 'uber',
        timeout: int = 15
    ) -> Optional[str]:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None,
            self.get_otp_from_email,
            email_client,
            target_email,
            service,
            timeout
        )


# ======================================================================
# main.py
# ======================================================================

import json
import uuid
import random
import asyncio
import os
from typing import Optional, Tuple, Dict, Any
from datetime import datetime
from urllib.parse import quote



FIRST_NAMES = [
    "Alexander", "Emma", "Benjamin", "Olivia", "Samuel", "Sophia",
    "Nathan", "Isabella", "Ethan", "Mia", "Lucas", "Charlotte",
    "Mason", "Amelia", "Logan", "Harper", "Jacob", "Evelyn",
    "Owen", "Abigail", "Sebastian", "Emily", "Henry", "Ella"
]

LAST_NAMES = [
    "Campbell", "Mitchell", "Roberts", "Carter", "Phillips", "Evans",
    "Turner", "Torres", "Parker", "Collins", "Edwards", "Stewart",
    "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan",
    "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson"
]


class AccountGenerator:
    def __init__(self, config: dict = None, assigned_proxy: str = None):
        self.config = config or {}
        self.request_handler = RequestHandler(config, assigned_proxy=assigned_proxy)
        self.device = DeviceProfile(self.request_handler)

    async def get_session(self):
        self.request_handler.reset_session()

        # upsert device 1 task 
        headers = {
            'x-uber-device-mobile-iso2': 'US',
            'x-uber-drm-id': self.device.drm_id,
            'x-uber-device': self.device.device_type,
            'x-uber-device-language': 'en_US',
            'user-agent': self.device.cronet_ua,
            'x-uber-device-os': self.device.os,
            'x-uber-device-sdk': self.device.sdk,
            'x-uber-request-uuid': str(uuid.uuid4()),
            'x-uber-client-user-session-id': self.device.client_user_analytics_session_id,
            'x-uber-client-version': self.device.version,
            'x-uber-device-manufacturer': self.device.manufacturer,
            'x-uber-call-uuid': self.device.call_uuid,
            'x-uber-device-id': self.device.udid,
            'x-uber-markup-textformat-version': '1',
            'x-uber-device-model': self.device.model,
            'uberctx-mobile-initiated': 'true',
            'x-uber-app-variant': self.device.app_variant,
            'x-uber-analytics-session-id': self.device.client_user_analytics_session_id,
            'content-type': 'application/json; charset=UTF-8',
            'uberctx-client-network-request-uuid': self.device.client_network_request_uuid,
            'x-uber-device-epoch': str(int(self.device._generate_epoch())),
            'uberctx-cold-launch-id': self.device.cold_launch_id,
            'x-uber-client-id': self.device.client_id,
            'x-uber-app-lifecycle-state': 'foreground',
            'x-uber-protocol-version': '0.73.0',
            'x-uber-device-timezone': self.device.location_city,
            'x-uber-client-name': 'eats',
            'x-uber-client-session': self.device.client_session_uuid,
            'x-uber-device-time-24-format-enabled': '0',
            'x-uber-app-device-id': self.device.app_device_id,
            'x-uber-device-voiceover': '0',
            'priority': 'u=1, i',
        }

        json_data = {
            'request': {
                'installationID': self.device.installation_uuid,
                'clientType': self.device.device_type,
                'clientIntegrityToken': '',
            },
        }

        response = await self.request_handler.post('Upsert Device 1', "https://cn-geo1.uber.com/rt/devices/task", headers=headers, data=json_data)

        # upsert device 2 results
        headers = {
            'x-uber-device-mobile-iso2': 'US',
            'x-uber-drm-id': self.device.drm_id,
            'x-uber-device': self.device.device_type,
            'x-uber-device-language': 'en_US',
            'user-agent': self.device.cronet_ua,
            'x-uber-device-os': self.device.os,
            'x-uber-device-sdk': self.device.sdk,
            'x-uber-request-uuid': self.device.client_network_request_uuid,
            'x-uber-client-user-session-id': self.device.client_user_analytics_session_id,
            'x-uber-client-version': self.device.version,
            'x-uber-device-manufacturer': self.device.manufacturer,
            'x-uber-call-uuid': self.device.call_uuid,
            'x-uber-device-id': self.device.udid,
            'x-uber-markup-textformat-version': '1',
            'x-uber-device-model': self.device.model,
            'uberctx-mobile-initiated': 'true',
            'x-uber-app-variant': self.device.app_variant,
            'x-uber-analytics-session-id': self.device.client_user_analytics_session_id,
            'content-type': 'application/json; charset=UTF-8',
            'x-uber-network-classifier': 'MEDIUM',
            'uberctx-client-network-request-uuid': self.device.client_network_request_uuid,
            'x-uber-device-epoch': str(int(self.device._generate_epoch())),
            'uberctx-cold-launch-id': self.device.cold_launch_id,
            'x-uber-client-id': self.device.client_id,
            'x-uber-app-lifecycle-state': 'foreground',
            'x-uber-protocol-version': '0.73.0',
            'x-uber-device-timezone': self.device.location_city,
            'x-uber-client-name': 'eats',
            'x-uber-client-session': self.device.client_session_uuid,
            'x-uber-device-time-24-format-enabled': '0',
            'x-uber-app-device-id': self.device.app_device_id,
            'x-uber-device-voiceover': '0',
            'priority': 'u=1, i',
        }

        json_data = {
            'request': {
                'installationID': self.device.installation_uuid,
                'msmAttestation': {
                    'token': self.device.generate_msm_attestation_token(),
                },
                'attemptNumber': 1,
            },
        }
        response = await self.request_handler.post('Upsert Device 2', "https://cn-geo1.uber.com/rt/devices/results", headers=headers, data=json_data)

        # upsert device 3 upsert
        headers = {
            'x-uber-device-mobile-iso2': 'US',
            'x-uber-device': self.device.device_type,
            'uber-trace-id': self.device.trace_id,
            'x-uber-device-language': 'en_US',
            'user-agent': self.device.user_agent,
            'x-uber-device-os': self.device.os,
            'x-uber-device-sdk': self.device.sdk,
            'x-uber-request-uuid': self.device.client_network_request_uuid,
            'x-uber-client-user-session-id': self.device.client_user_analytics_session_id,
            'x-uber-client-version': self.device.version,
            'x-uber-device-manufacturer': self.device.manufacturer,
            'x-uber-call-uuid': self.device.call_uuid,
            'x-uber-device-id': self.device.udid,
            'x-uber-markup-textformat-version': '1',
            'x-uber-device-model': self.device.model,
            'uberctx-mobile-initiated': 'true',
            'x-uber-app-variant': self.device.app_variant,
            'x-uber-analytics-session-id': self.device.client_user_analytics_session_id,
            'content-type': 'application/json; charset=UTF-8',
            'uberctx-client-network-request-uuid': self.device.client_network_request_uuid,
            'x-uber-device-epoch': str(int(self.device._generate_epoch())),
            'uberctx-cold-launch-id': self.device.cold_launch_id,
            'x-uber-client-id': self.device.client_id,
            'x-uber-app-lifecycle-state': 'foreground',
            'x-uber-protocol-version': '0.73.0',
            'x-uber-device-timezone': self.device.location_city,
            'x-uber-client-name': 'eats',
            'x-uber-client-session': self.device.client_session_uuid,
            'x-uber-device-time-24-format-enabled': '0',
            'x-uber-app-device-id': self.device.app_device_id,
            'x-uber-device-voiceover': '0',
            'priority': 'u=1, i',
        }

        json_data = {
            "deviceData": self.device.build_device_data_v2()
        }

        await self.request_handler.post(
            'Upsert Device 3',
            url="https://cn-geo1.uber.com/rt/devices/upsert",
            headers=headers,
            data=json_data
        )

        headers = {
            'sec-ch-ua': '"Chromium";v="142", "Android WebView";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'upgrade-insecure-requests': '1',
            'user-agent': self.device.user_agent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'x-uber-client-id': self.device.client_id,
            'x-uber-pwv-instance-id': str(uuid.uuid4()),
            'sec-ch-prefers-color-scheme': 'light',
            'x-uber-auth-social-login-providers': '["googleweb","google"]',
            'x-uber-device-data': self.device.build_device_data(),
            'x-uber-pwv-client-id': 'identity_eats_usl',
            'x-requested-with': self.device.client_id,
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=0, i',
        }

        params = {
            'showDebugInfo': 'false',
            'x-uber-device': self.device.device_type,
            'x-uber-client-name': 'eats',
            'x-uber-client-version': self.device.version,
            'x-uber-client-id': self.device.client_id,
            'firstPartyClientID': self.device.first_party_client_id,
            'isEmbedded': 'true',
            'codeChallenge': self.device.pkce_challenge,
            'app_url': self.device.app_url,
            'asms': 'true',
            'x-uber-device-udid': self.device.udid,
            'sim_mcc': '',
            'sim_mnc': '',
            'x-uber-app-device-id': self.device.app_device_id,
            'x-uber-device-location-latitude': self.device.latitude,
            'x-uber-device-location-longitude': self.device.longitude,
            'socialNative': 'g',
            'x-uber-cold-launch-id': self.device.cold_launch_id,
            'x-uber-hot-launch-id': self.device.hot_launch_id,
            'x-uber-app-variant': self.device.app_variant,
            'countryCode': 'US',
            'known_user': 'false',
            'isChromeCustomTabSession': 'false',
        }

        referer_items = []
        for k, v in params.items():
            if k == 'app_url':
                referer_items.append(f"{k}={quote(str(v), safe='')}")
            else:
                referer_items.append(f"{k}={v}")
        referer_url = 'https://auth.uber.com/v2?' + '&'.join(referer_items)
        
        await self.request_handler.get("Get Session", "https://auth.uber.com/v2", headers=headers, params=params)

        # get udi-fingerprint
        headers = {
            'sec-ch-ua-platform': '"Android"',
            'x-csrf-token': 'x',
            'user-agent': self.device.user_agent,
            'sec-ch-ua': '"Android WebView";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'content-type': 'application/json',
            'sec-ch-ua-mobile': '?1',
            'accept': '*/*',
            'origin': 'https://auth.uber.com',
            'x-requested-with': self.device.client_id,
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': referer_url,
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=1, i',
        }

        json_data = {
            'meta': self.device.get_device_fingerprint()
        }

        await self.request_handler.post('Get UDI Fingerprint', 'https://auth.uber.com/v2/udi-meta', headers=headers, data=json_data)

    async def email_signup(self, email: str) -> Optional[str]:
        json_data = {
            'formContainerAnswer': {
                'inAuthSessionID': '',
                'formAnswer': {
                    'flowType': 'INITIAL',
                    'standardFlow': True,
                    'accountManagementFlow': False,
                    'daffFlow': False,
                    'productConstraints': {
                        'autoSMSVerificationSupported': True,
                        'isEligibleForWebOTPAutofill': False,
                        'uslFELibVersion': '',
                        'uslMobileLibVersion': '',
                        'isWhatsAppAvailable': False,
                        'isPublicKeyCredentialSupported': True,
                        'isAppleAvailable': False,
                        'isFacebookAvailable': False,
                        'isGoogleAvailable': False,
                        'isRakutenAvailable': False,
                        'isKakaoAvailable': False,
                    },
                    'additionalParams': {
                        'isEmailUpdatePostAuth': False,
                    },
                    'deviceData': self.device.build_device_data(),
                    'codeChallenge': self.device.pkce_challenge,
                    'uslURL': self.device.build_usl_url(),
                    'firstPartyClientID': self.device.first_party_client_id,
                    'screenAnswers': [
                        {
                            'screenType': 'PHONE_NUMBER_INITIAL',
                            'eventType': 'TypeInputEmail',
                            'fieldAnswers': [
                                {
                                    'fieldType': 'EMAIL_ADDRESS',
                                    'emailAddress': email,
                                },
                            ],
                        },
                    ],
                    'appContext': {
                        'appUrl': self.device.app_url,
                        'socialNative': 'g',
                    },
                },
            },
        }
        
        headers = {
            'sec-ch-ua-platform': '"Android"',
            'x-uber-hot-launch-id': self.device.hot_launch_id,
            #'x-uber-challenge-provider': 'ARKOSE_TOKEN',
            'sec-ch-ua': '"Chromium";v="142", "Android WebView";v="142", "Not_A Brand";v="99"',
            'x-uber-device-location-longitude': self.device.longitude,
            'sec-ch-ua-mobile': '?1',
            'x-uber-client-name': 'eats',
            #'x-uber-challenge-token': '678187f84f1554b76.6387716002|r=us-west-2|meta=3|metabgclr=transparent|metaiconclr=%23757575|guitextcolor=%23000000|pk=30000F36-CADF-490C-929A-C6A7DD8B33C4|at=40|sup=1|rid=5|ag=101|cdn_url=https%3A%2F%2Fak04a6qc.uber.com%2Fcdn%2Ffc|surl=https%3A%2F%2Fak04a6qc.uber.com|smurl=https%3A%2F%2Fak04a6qc.uber.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager',
            'x-uber-request-uuid': str(uuid.uuid4()),
            'x-uber-app-device-id': self.device.app_device_id,
            'x-uber-app-variant': self.device.app_variant,
            'content-type': 'application/json',
            'x-uber-device': self.device.device_type,
            'x-csrf-token': 'x',
            'x-uber-cold-launch-id': self.device.cold_launch_id,
            'x-uber-device-udid': self.device.udid,
            'accept-language': 'en',
            'x-uber-usl-id': self.device.udid,
            'x-uber-device-location-latitude': self.device.latitude,
            'x-uber-client-version': self.device.version,
            'user-agent': self.device.user_agent,
            'x-uber-client-id': self.device.client_id,
            'accept': '*/*',
            'origin': 'https://auth.uber.com',
            'x-requested-with': self.device.client_id,
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': self.device.build_usl_url(),
            'priority': 'u=1, i',
        }

        """
        cookies = {
            '_cc': 'AcWQI%2FVRsGGasJLDQCpGie66',
            '_cid_cc': 'AcWQI%2FVRsGGasJLDQCpGie66',
            '_ua': '{"session_id":"fa153bf6-1425-4700-8fb4-02184a87655b","session_time_ms":1764711506103}',
            'udi-fingerprint': 'w5UnWL+SLhGOkmgubZD3/XEuAMKnY1hRi3yWdikE6fooNmc2eYNB5HwiQdtsq9O+Jl0k2d88Q4+HxbN6VZDYuQ==7BaOiGUaoSFvcz4lYOw82P1owRIhjr6psRVQGPVt5DA=',
        }
        """

        response = await self.request_handler.post(
            "Email Signup",
            "https://auth.uber.com/v2/submit-form",
            headers,
            json_data
        )

        if response:
            try:
                if not response.text or response.text.strip() == '':
                    print(f"[!] Email Signup: Empty response body")
                    return None
                return response.json().get('inAuthSessionID')
            except json.JSONDecodeError as e:
                print(f"[!] Email Signup: Invalid JSON response - {e}")
                print(f"    Response text: {response.text[:200]}")
                return None
        return None

    async def submit_otp(self, session_id: str, otp: str) -> Optional[Dict[str, Any]]:
        json_data = {
            'formContainerAnswer': {
                'inAuthSessionID': session_id,
                'formAnswer': {
                    'flowType': 'SIGN_UP',
                    'standardFlow': True,
                    'accountManagementFlow': False,
                    'daffFlow': False,
                    'productConstraints': {
                        'autoSMSVerificationSupported': True,
                        'isEligibleForWebOTPAutofill': False,
                        'uslFELibVersion': '',
                        'uslMobileLibVersion': '',
                        'isWhatsAppAvailable': False,
                        'isPublicKeyCredentialSupported': False,
                        'isAppleAvailable': False,
                        'isFacebookAvailable': False,
                        'isGoogleAvailable': False,
                        'isRakutenAvailable': False,
                        'isKakaoAvailable': False,
                        'isGoogleDeeplinkAvailable': True,
                    },
                    'additionalParams': {
                        'isEmailUpdatePostAuth': False,
                    },
                    'deviceData': self.device.build_device_data(),
                    'codeChallenge': self.device.pkce_challenge,
                    'uslURL': self.device.build_usl_url(),
                    'firstPartyClientID': self.device.first_party_client_id,
                    'screenAnswers': [
                        {
                            'screenType': 'EMAIL_OTP_CODE',
                            'eventType': 'TypeEmailOTP',
                            'fieldAnswers': [
                                {
                                    'fieldType': 'EMAIL_OTP_CODE',
                                    'emailOTPCode': otp,
                                },
                            ],
                        },
                    ],
                },
            },
        }

        headers = {
            'X-Uber-Usl-Id': self.device.udid,
            'X-Uber-Hot-Launch-Id': self.device.hot_launch_id,
            'x-uber-device-location-latitude': self.device.latitude,
            'X-Uber-Request-Uuid': str(uuid.uuid4()),
            'Accept-Language': 'en',
            'X-Uber-Device-Udid': self.device.udid,
            'X-Uber-Client-Name': 'eats',
            'X-Uber-Device': self.device.device_type,
            'X-Uber-Client-Version': self.device.version,
            'X-Uber-App-Variant': self.device.app_variant,
            'X-Uber-Cold-Launch-Id': self.device.cold_launch_id,
            'X-Uber-Client-Id': self.device.client_id,
            'User-Agent': self.device.user_agent,
            'Content-Type': 'application/json',
            'X-Uber-App-Device-Id': self.device.app_device_id,
            'x-uber-device-location-longitude': self.device.longitude,
            'Accept': '*/*',
            'Origin': 'https://auth.uber.com',
            'X-Requested-With': self.device.client_id,
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://auth.uber.com/',
        }

        response = await self.request_handler.post(
            "Submit OTP",
            "https://cn-geo1.uber.com/rt/silk-screen/submit-form",
            headers,
            json_data
        )

        if response:
            return response.json()
        return None

    async def _skip_phone_number(self, session_id: str) -> Optional[str]:
        """
        Function: Skip phone number screen
        On signup, some times submit_otp results in the next step being PHONE_NUMBER_PROGRESSIVE, rather than FULL_NAME_PROGRESSIVE.
        To handle this, only on these cases do we call _skip_phone_number to handle this phone number screen issue.
        """

        headers = {
            'X-Uber-Usl-Id': self.device.udid,
            'X-Uber-Hot-Launch-Id': self.device.hot_launch_id,
            'X-Uber-Device-Location-Latitude': self.device.latitude,
            'X-Uber-Request-Uuid': str(uuid.uuid4()),
            'Accept-Language': 'en',
            'X-Uber-Device-Udid': self.device.udid,
            'X-Uber-Client-Name': 'eats',
            'X-Uber-Device': self.device.device_type,
            'X-Uber-Client-Version': self.device.version,
            'X-Uber-App-Variant': self.device.app_variant,
            'X-Uber-Cold-Launch-Id': self.device.cold_launch_id,
            'X-Uber-Client-Id': self.device.client_id,
            'User-Agent': self.device.user_agent,
            'Content-Type': 'application/json',
            'X-Uber-App-Device-Id': self.device.app_device_id,
            'X-Uber-Device-Location-Longitude': self.device.longitude,
            'Accept': '*/*',
            'Origin': 'https://auth.uber.com',
            'X-Requested-With': self.device.client_id,
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://auth.uber.com/',
        }

        json_data = {
            'formContainerAnswer': {
                'inAuthSessionID': session_id,
                'formAnswer': {
                    'flowType': 'PROGRESSIVE_SIGN_UP',
                    'standardFlow': True,
                    'accountManagementFlow': False,
                    'daffFlow': False,
                    'productConstraints': {
                        'autoSMSVerificationSupported': True,
                        'isEligibleForWebOTPAutofill': False,
                        'uslFELibVersion': '',
                        'uslMobileLibVersion': '',
                        'isWhatsAppAvailable': False,
                        'isPublicKeyCredentialSupported': False,
                        'isAppleAvailable': False,
                        'isFacebookAvailable': False,
                        'isGoogleAvailable': False,
                        'isRakutenAvailable': False,
                        'isKakaoAvailable': False,
                        'isGoogleDeeplinkAvailable': True,
                    },
                    'additionalParams': {
                        'isEmailUpdatePostAuth': False,
                    },
                    'deviceData': self.device.build_device_data(),
                    'codeChallenge': self.device.pkce_challenge,
                    'uslURL': self.device.build_usl_url(),
                    'firstPartyClientID': self.device.first_party_client_id,
                    'screenAnswers': [
                        {
                            'screenType': 'SKIP',
                            'eventType': 'TypeSkip',
                            'fieldAnswers': [],
                        },
                    ],
                },
            },
        }

        response = await self.request_handler.post(
            "Skip Phone Number",
            "https://cn-geo1.uber.com/rt/silk-screen/submit-form",
            headers,
            json_data
        )

        if response:
            return response.json().get('inAuthSessionID')
        return None

    async def _submit_name(self, session_id: str, name: str) -> Optional[str]:
        first_name, last_name = name.split(' ', 1)

        json_data = {
            'formContainerAnswer': {
                'inAuthSessionID': session_id,
                'formAnswer': {
                    'flowType': 'PROGRESSIVE_SIGN_UP',
                    'standardFlow': True,
                    'accountManagementFlow': False,
                    'daffFlow': False,
                    'productConstraints': {
                        'autoSMSVerificationSupported': True,
                        'isEligibleForWebOTPAutofill': False,
                        'uslFELibVersion': '',
                        'uslMobileLibVersion': '',
                        'isWhatsAppAvailable': False,
                        'isPublicKeyCredentialSupported': False,
                        'isAppleAvailable': False,
                        'isFacebookAvailable': False,
                        'isGoogleAvailable': False,
                        'isRakutenAvailable': False,
                        'isKakaoAvailable': False,
                        'isGoogleDeeplinkAvailable': True,
                    },
                    'additionalParams': {
                        'isEmailUpdatePostAuth': False,
                    },
                    'deviceData': self.device.build_device_data(),
                    'uslURL': self.device.build_usl_url(),
                    'firstPartyClientID': self.device.first_party_client_id,
                    'screenAnswers': [
                        {
                            'screenType': 'FULL_NAME_PROGRESSIVE',
                            'eventType': 'TypeInputNewUserFullName',
                            'fieldAnswers': [
                                {
                                    'fieldType': 'FIRST_NAME',
                                    'firstName': first_name,
                                },
                                {
                                    'fieldType': 'LAST_NAME',
                                    'lastName': last_name,
                                },
                            ],
                        },
                    ],
                },
            },
        }

        headers = {
            'X-Uber-Usl-Id': self.device.udid,
            'X-Uber-Hot-Launch-Id': self.device.hot_launch_id,
            'x-uber-device-location-longitude': self.device.latitude,
            'X-Uber-Request-Uuid': str(uuid.uuid4()),
            'Accept-Language': 'en',
            'X-Uber-Device-Udid': self.device.udid,
            'X-Uber-Client-Name': 'eats',
            'X-Uber-Device': self.device.device_type,
            'X-Uber-Client-Version': self.device.version,
            'X-Uber-App-Variant': self.device.app_variant,
            'X-Uber-Cold-Launch-Id': self.device.cold_launch_id,
            'X-Uber-Client-Id': self.device.client_id,
            'User-Agent': self.device.user_agent,
            'Content-Type': 'application/json',
            'X-Uber-App-Device-Id': self.device.app_device_id,
            'x-uber-device-location-longitude': self.device.longitude,
            'Accept': '*/*',
            'Origin': 'https://auth.uber.com',
            'X-Requested-With': self.device.client_id,
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://auth.uber.com/',
        }

        response = await self.request_handler.post(
            "Submit Name",
            "https://cn-geo1.uber.com/rt/silk-screen/submit-form",
            headers,
            json_data
        )

        if response:
            return response.json().get('inAuthSessionID')
        return None

    async def _submit_legal_confirmation(self, session_id: str) -> Tuple[Optional[str], Optional[str]]:
        json_data = {
            'formContainerAnswer': {
                'inAuthSessionID': session_id,
                'formAnswer': {
                    'flowType': 'SIGN_UP',
                    'standardFlow': True,
                    'accountManagementFlow': False,
                    'daffFlow': False,
                    'productConstraints': {
                        'autoSMSVerificationSupported': True,
                        'isEligibleForWebOTPAutofill': False,
                        'uslFELibVersion': '',
                        'uslMobileLibVersion': '',
                        'isWhatsAppAvailable': False,
                        'isPublicKeyCredentialSupported': False,
                        'isAppleAvailable': False,
                        'isFacebookAvailable': False,
                        'isGoogleAvailable': False,
                        'isRakutenAvailable': False,
                        'isKakaoAvailable': False,
                        'isGoogleDeeplinkAvailable': True,
                    },
                    'additionalParams': {
                        'isEmailUpdatePostAuth': False,
                    },
                    'deviceData': self.device.build_device_data(),
                    'uslURL': self.device.build_usl_url(),
                    'firstPartyClientID': self.device.first_party_client_id,
                    'screenAnswers': [
                        {
                            'screenType': 'LEGAL',
                            'eventType': 'TypeSignupLegal',
                            'fieldAnswers': [
                                {
                                    'fieldType': 'LEGAL_CONFIRMATION',
                                    'legalConfirmation': True,
                                },
                                {
                                    'fieldType': 'LEGAL_CONFIRMATIONS',
                                    'legalConfirmations': {
                                        'legalConfirmations': [
                                            {
                                                'disclosureVersionUUID': 'ef1d61c9-b09e-4d44-8cfb-ddfa15cc7523',
                                                'isAccepted': True,
                                            },
                                        ],
                                    },
                                },
                            ],
                        },
                    ],
                },
            },
        }

        headers = {
            'X-Uber-Usl-Id': self.device.udid,
            'X-Uber-Hot-Launch-Id': self.device.hot_launch_id,
            'x-uber-device-location-latitude': self.device.latitude,
            'X-Uber-Request-Uuid': str(uuid.uuid4()),
            'Accept-Language': 'en',
            'X-Uber-Device-Udid': self.device.udid,
            'X-Uber-Client-Name': 'eats',
            'X-Uber-Device': self.device.device_type,
            'X-Uber-Client-Version': self.device.version,
            'X-Uber-App-Variant': self.device.app_variant,
            'X-Uber-Cold-Launch-Id': self.device.cold_launch_id,
            'X-Uber-Client-Id': self.device.client_id,
            'User-Agent': self.device.user_agent,
            'Content-Type': 'application/json',
            'X-Uber-App-Device-Id': self.device.app_device_id,
            'x-uber-device-location-longitude': self.device.longitude,
            'Accept': '*/*',
            'Origin': 'https://auth.uber.com',
            'X-Requested-With': self.device.client_id,
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://auth.uber.com/',
        }

        response = await self.request_handler.post(
            "Submit Legal",
            "https://cn-geo1.uber.com/rt/silk-screen/submit-form",
            headers,
            json_data
        )

        if response:
            resp_json = response.json()
            try:
                fields = resp_json.get('form', {}).get('screens', [{}])[0].get('fields', [])
                auth_code = fields[0].get('authCode') if fields else None
                session_id = resp_json.get('inAuthSessionID')
                return session_id, auth_code
            except (IndexError, KeyError):
                print("[!] Failed to extract auth code")
                return None, None

        return None, None

    async def _submit_auth_code(self, session_id: str, auth_code: str, email: str = '', name: str = '') -> Tuple[bool, Optional[dict]]:
        json_data = {
            'formContainerAnswer': {
                'inAuthSessionID': f'{session_id}.{auth_code}',
                'formAnswer': {
                    'flowType': 'SIGN_IN',
                    'screenAnswers': [
                        {
                            'screenType': 'SESSION_VERIFICATION',
                            'fieldAnswers': [
                                {
                                    'fieldType': 'SESSION_VERIFICATION_CODE',
                                    'sessionVerificationCode': auth_code,
                                },
                                {
                                    'fieldType': 'CODE_VERIFIER',
                                    'codeVerifier': self.device.pkce_verifier,
                                },
                            ],
                            'eventType': 'TypeVerifySession',
                        },
                    ],
                    'deviceData': self.device.build_device_data(),
                    'firstPartyClientID': self.device.first_party_client_id,
                    'standardFlow': True,
                    'appID': 'EATS',
                },
            },
        }

        headers = {
            'X-Uber-Device-Mobile-Iso2': self.device.location_country,
            'X-Uber-Drm-Id': self.device.drm_id,
            'X-Uber-Device': self.device.device_type,
            'X-Uber-Cit': self.device.build_cit_token(),
            'X-Uber-Device-Language': f'en_{self.device.location_country}',
            'User-Agent': self.device.cronet_ua,
            'X-Uber-Device-Os': self.device.os,
            'X-Uber-Device-Sdk': self.device.sdk,
            'X-Uber-Request-Uuid': str(uuid.uuid4()),
            'X-Uber-Client-User-Session-Id': self.device.client_user_analytics_session_id,
            'X-Uber-Client-Version': self.device.version,
            'X-Uber-Device-Manufacturer': self.device.manufacturer,
            'X-Uber-Call-Uuid': str(uuid.uuid4()),
            'X-Uber-Device-Id': self.device.udid,
            'X-Uber-Markup-Textformat-Version': '1',
            'X-Uber-Device-Model': self.device.model,
            'Uberctx-Mobile-Initiated': 'true',
            'X-Uber-App-Variant': self.device.app_variant,
            'X-Uber-Analytics-Session-Id': self.device.client_user_analytics_session_id,
            'X-Uber-Sig-Params': 'a=ES256;v=1',
            'Content-Type': 'application/json; charset=UTF-8',
            'X-Uber-Network-Classifier': 'MEDIUM',
            'Uberctx-Client-Network-Request-Uuid': str(uuid.uuid4()),
            'X-Uber-Device-Epoch': str(int(self.device._generate_epoch())),
            'Uberctx-Cold-Launch-Id': self.device.cold_launch_id,
            'X-Uber-Client-Id': self.device.client_id,
            'X-Uber-App-Lifecycle-State': 'foreground',
            'X-Uber-Protocol-Version': '0.73.0',
            'X-Uber-Device-Timezone': self.device.location_city,
            'X-Uber-Client-Name': 'eats', # stays as eats even for postmates
            'X-Uber-Client-Session': str(uuid.uuid4()),
            'X-Uber-Device-Time-24-Format-Enabled': '0',
            'X-Uber-App-Device-Id': self.device.app_device_id,
            'X-Uber-Device-Voiceover': '0',
            'Priority': 'u=1, i',
        }
        headers['X-Uber-Sig'] = self.device.build_sig_token(headers)

        response = await self.request_handler.post(
            "Submit Auth Code",
            "https://cn-geo1.uber.com/rt/silk-screen/submit-form",
            headers,
            json_data
        )

        if response:
            resp_json = response.json()
            return True, resp_json
        else:
            return False, None
    
    async def finish_signup(self, auth_code):
        # get user id token
        headers = {
            'x-uber-device-mobile-iso2': 'US',
            'x-uber-drm-id': self.device.drm_id,
            'x-uber-device': self.device.device_type,
            'x-uber-device-language': 'en_US',
            'user-agent': self.device.cronet_ua,
            'authorization': f'Bearer {auth_code}',
            'x-uber-device-os': self.device.os,
            'x-uber-device-sdk': self.device.sdk,
            'x-uber-request-uuid': str(uuid.uuid4()),
            'x-uber-client-user-session-id': self.device.client_user_analytics_session_id,
            'x-uber-client-version': self.device.version,
            'x-uber-device-manufacturer': self.device.manufacturer,
            'x-uber-call-uuid': self.device.call_uuid,
            'x-uber-device-id': self.device.udid,
            'x-uber-markup-textformat-version': '1',
            'x-uber-device-model': self.device.model,
            'uberctx-mobile-initiated': 'true',
            'x-uber-app-variant': self.device.app_variant,
            'x-uber-analytics-session-id': self.device.client_user_analytics_session_id,
            'content-type': 'application/json; charset=UTF-8',
            'x-uber-network-classifier': 'MEDIUM',
            'x-uber-token': 'no-token',
            'uberctx-client-network-request-uuid': self.device.client_network_request_uuid,
            'x-uber-device-epoch': str(int(self.device._generate_epoch())),
            'uberctx-cold-launch-id': self.device.cold_launch_id,
            'x-uber-client-id': self.device.client_id,
            'x-uber-app-lifecycle-state': 'foreground',
            'x-uber-protocol-version': '0.73.0',
            'x-uber-device-timezone': self.device.location_city,
            'x-uber-client-name': 'eats',
            'x-uber-client-session': self.device.client_session_uuid,
            'x-uber-device-time-24-format-enabled': '0',
            'x-uber-app-device-id': self.device.app_device_id,
            'x-uber-device-voiceover': '0',
            'priority': 'u=1, i',
        }

        json_data = {
            'request': {
                'clientID': self.device.first_party_client_id,
                'skipSigning': True,
            },
        }

        await self.request_handler.post('get cookie id token', 'https://cn-geo1.uber.com/rt/identity/oauth2/user-id-token', headers=headers, data=json_data)


        # GSU
        device_data_header = json.loads(self.device.build_device_data())
        headers = {
            'sec-ch-ua': '"Android WebView";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'upgrade-insecure-requests': '1',
            'user-agent': self.device.user_agent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'x-uber-device-mobile-iso2': 'US',
            'x-uber-drm-id': self.device.drm_id,
            'x-uber-device': self.device.device_type,
            'x-uber-cold-launch-id': self.device.cold_launch_id,
            'sec-ch-prefers-color-scheme': 'light',
            'x-uber-device-language': 'en_US',
            'x-uber-device-os': self.device.os,
            'x-uber-device-sdk': self.device.sdk,
            'x-uber-request-uuid': str(uuid.uuid4()),
            'x-uber-client-version': self.device.version,
            'x-uber-client-user-session-id': self.device.client_user_analytics_session_id,
            'x-uber-device-manufacturer': self.device.manufacturer,
            'x-uber-device-id': self.device.udid,
            'x-uber-hot-launch-id': self.device.hot_launch_id,
            'x-uber-device-model': self.device.model,
            'x-uber-app-variant': self.device.app_variant,
            'x-uber-device-data': device_data_header,
            'x-uber-device-udid': self.device.udid,
            'x-uber-device-epoch': str(int(self.device.device_epoch)),
            'x-uber-client-id': self.device.client_id,
            'x-uber-device-timezone': self.device.location_city,
            'x-uber-pwv-instance-id': str(uuid.uuid4()),
            'x-uber-client-name': 'eats',
            'x-uber-client-session': self.device.client_session_uuid,
            'x-uber-pwv-client-id': 'identity_eats_uam',
            'x-uber-app-device-id': self.device.app_device_id,
            'x-requested-with': self.device.client_id,
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=0, i',
        }

        params = [
            ('entry_ctx', 'usl_email_first_signup_optional'),
            ('entry_domain', 'auth.uber.com'),
            ('type', '11'),
            ('host_theme', 'light'),
            ('type', '11'),
        ]

        await self.request_handler.get('GSU', 'https://account.uber.com/gsu', headers=headers, params=params)

    async def create_account_hotmail(self, hotmail_account: str, hotmail_client_key: str, sleep: int = 5, apply_promo: bool = False) -> Optional[dict]:
        """Create account using Hotmail for OTP verification"""
        await self.device.initialize()

        with open('config.json', 'r') as f:
            config = json.load(f)

        parts = hotmail_account.split(':')
        if len(parts) < 4:
            print("[!] Invalid hotmail account format. Expected: email:password:token:uuid")
            return None

        hotmail_email = parts[0]

        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        name = f"{first_name} {last_name}"

        print(f"\n[*] Creating account using hotmail: {hotmail_email}")
        await self.get_session()

        await asyncio.sleep(sleep)

        session_id = await self.email_signup(hotmail_email)
        if not session_id:
            print("[!] Failed to initiate signup")
            return None

        print("[*] Waiting for OTP...")
        await asyncio.sleep(sleep)

        try:
            hotmail_client = HotmailClient(
                account=hotmail_account,
                client_key=hotmail_client_key
            )

            otp_extractor = EmailOTPExtractor()
            otp = await otp_extractor.get_otp_async(
                email_client=hotmail_client,
                target_email=hotmail_email,
                service='uber',
                timeout=60
            )

            if not otp:
                print("[!] Failed to retrieve OTP")
                return None
        except BannedAccountException as e:
            print(f"[!] Hotmail account is banned: {e}")
            return None
        except Exception as e:
            print(f"[!] Error getting OTP: {e}")
            return None

        print(f"[✓] OTP received: {otp}")

        # Submit OTP
        response = await self.submit_otp(session_id, otp)
        flow_type = response.get('form', {}).get('screens', [{}])[0].get('screenType', '')
        session_id = response.get('inAuthSessionID', None)
        if not session_id:
            print("[!] Failed to verify OTP")
            return None

        await asyncio.sleep(sleep)

        # if flow is phone number progressive, trigger skip phone number function
        if flow_type == 'PHONE_NUMBER_PROGRESSIVE':
            session_id = await self._skip_phone_number(session_id)
            if not session_id:
                print("[!] Failed to skip phone number")
                return None

        # Submit name
        session_id = await self._submit_name(session_id, name)
        if not session_id:
            print("[!] Failed to submit name")
            return None

        await asyncio.sleep(sleep)

        # Submit legal confirmation
        session_id, auth_code = await self._submit_legal_confirmation(session_id)
        if not session_id or not auth_code:
            print("[!] Failed to submit legal confirmation")
            return None

        await asyncio.sleep(sleep)

        # Submit auth code and get final response
        success, resp_json = await self._submit_auth_code(session_id, auth_code, hotmail_email, name)
        if not success:
            print("[!] Failed to complete registration")
            return None

        # set cookies
        self.cookies = resp_json['cookies']
        for cookie in resp_json["cookies"]:
            self.request_handler.session.cookies.set(
                name=cookie["name"],
                value=cookie["value"],
                domain=cookie["domain"],
                path=cookie.get("path", "/"),
                secure=True
            )

        # get necessary data
        self.auth_token = resp_json['oAuthInfo']['accessToken']
        self.refresh_token = resp_json['oAuthInfo']['refreshToken']
        self.sid = resp_json['cookies'][0]['value']
        self.user_uuid = resp_json['userUUID']

        await self.finish_signup(self.auth_token)

        self.account_manager = AccountManager(self.request_handler, self.device, self.sid, self.auth_token, self.user_uuid)

        if apply_promo:
            await self.account_manager.apply_promo(config['promos']['promo_code'])

        print("[✓] Account created successfully!")

        return resp_json, flow_type

async def process_single_hotmail_account(config: dict, idx: int, total: int, proxies_list: list, hotmail_accounts: list) -> dict:
    if not hotmail_accounts:
        print("[!] No hotmail accounts available")
        return {
            'success': False,
            'email': 'N/A',
            'error': 'No hotmail accounts available'
        }

    hotmail_account = hotmail_accounts.pop(0)
    hotmail_email = hotmail_account.split(':')[0]

    try:
        hotmail_file = 'hotmail_accounts.txt'
        if os.path.exists(hotmail_file):
            with open(hotmail_file, 'r') as f:
                lines = f.readlines()

            with open(hotmail_file, 'w') as f:
                for line in lines:
                    if line.strip() != hotmail_account:
                        f.write(line)

            print(f"[✓] Removed {hotmail_email} from {hotmail_file}")
    except Exception as e:
        print(f"[!] Warning: Failed to remove account from file: {e}")

    print(f"\n{'='*60}")
    print(f"[*] Processing account {idx}/{total} using hotmail: {hotmail_email}")
    print(f"{'='*60}")

    assigned_proxy = None
    if config.get('proxies_enabled', False) and proxies_list:
        if len(proxies_list) > 0:
            assigned_proxy = proxies_list.pop(random.randint(0, len(proxies_list) - 1))
            print(f"[*] Assigned proxy to account {idx}: {assigned_proxy[:30]}...")
            RequestHandler.remove_proxy_from_file(assigned_proxy)
        else:
            print(f"[!] No proxies left for account {idx}, proceeding without proxy")

    generator = AccountGenerator(config, assigned_proxy=assigned_proxy)
    hotmail_client_key = config.get('hotmail_client_key', '')

    if not hotmail_client_key:
        print("[!] hotmail_client_key not found in config.json")
        return {
            'success': False,
            'email': hotmail_email,
            'error': 'hotmail_client_key not configured'
        }

    try:
        # Step 1: Create account using hotmail
        response, flow_type = await generator.create_account_hotmail(
            hotmail_account,
            hotmail_client_key,
            sleep=config.get('sleep', 5),
            apply_promo=config['promos']['apply_promo']
        )

        if not response:
            print(f"[!] Failed to create account using hotmail: {hotmail_email}")
            return {
                'success': False,
                'email': hotmail_email,
                'error': 'Account creation failed'
            }

        # Save Details
        result_email = response.get('userProfile', {}).get('email', hotmail_email)
        print(f"[✓] Successfully created Uber account for: {result_email}")
        account_info = {
            'email': result_email,
            'hotmail_account': hotmail_account,
            'flow_type': flow_type,
            'timezone': generator.device.location_city,
            'longitude': generator.device.longitude,
            'latitude': generator.device.latitude,
            'model': generator.device.model,
            'phone_name': generator.device.phone_name,
            'brand': generator.device.brand,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }

        # save local data
        if config.get('app_variant') == 'ubereats':
            with open('genned/genned_accounts.json', 'r+') as f:
                data = json.load(f)
                data['accounts'].append(account_info)
                f.seek(0)
                f.truncate()
                json.dump(data, f, indent=4)
        elif config.get('app_variant') == 'postmates':
            with open('genned/postmates_genned.json', 'r+') as f:
                data = json.load(f)
                data['accounts'].append(account_info)
                f.seek(0)
                f.truncate()
                json.dump(data, f, indent=4)

        # save data for production
        account_info['auth_token'] = generator.auth_token
        account_info['refresh_token'] = generator.refresh_token
        account_info['cookies'] = generator.cookies

        with open('genned/genned_accounts_production.json', 'r+') as f:
            data = json.load(f)
            data['accounts'].append(account_info)
            f.seek(0)
            f.truncate()
            json.dump(data, f, indent=4)

        return {
            'success': True,
            'email': result_email,
            'hotmail_account': hotmail_account,
            'error': None
        }
    except Exception as e:
        print(f"[!] Error processing {hotmail_email}: {e}")
        return {
            'success': False,
            'email': hotmail_email,
            'error': str(e)
        }


async def main():
    with open('config.json', 'r') as f:
        config = json.load(f)

    if not config.get('hotmail_client_key'):
        print("[!] hotmail_client_key not found in config.json")
        return

    hotmail_file = 'hotmail_accounts.txt'
    if not os.path.exists(hotmail_file):
        print(f"[!] {hotmail_file} not found")
        print(f"[!] Please create {hotmail_file} with hotmail accounts (one per line)")
        print(f"[!] Format: email:password:token:uuid")
        return

    with open(hotmail_file, 'r') as f:
        hotmail_accounts = [line.strip() for line in f.readlines() if line.strip()]

    if not hotmail_accounts:
        print(f"[!] No hotmail accounts found in {hotmail_file}")
        return

    print(f"[✓] Loaded {len(hotmail_accounts)} hotmail accounts")
    
    proxies_list = []
    if config.get('proxies_enabled', False):
        proxies_list = RequestHandler.load_proxies()
        if proxies_list:
            print(f'[✓] Loaded {len(proxies_list)} proxies from proxies.txt')
        else:
            print('[!] Proxies enabled but none loaded, proceeding without proxies')
            config['proxies_enabled'] = False
    
    num_of_accounts_to_generate = input("Enter number of accounts to generate: ")

    try:
        num_of_accounts_to_generate = int(num_of_accounts_to_generate)
        if num_of_accounts_to_generate <= 0:
            print("[!] Invalid number. Must be greater than 0.")
            return
    except ValueError:
        print("[!] Invalid input. Please enter a number.")
        return

    if num_of_accounts_to_generate > len(hotmail_accounts):
        print(f"[!] Warning: Only {len(hotmail_accounts)} hotmail accounts available for {num_of_accounts_to_generate} requested")
        print(f"[!] Will generate {len(hotmail_accounts)} accounts")
        num_of_accounts_to_generate = len(hotmail_accounts)

    print(f"[*] Generating {num_of_accounts_to_generate} accounts")

    if config.get('proxies_enabled', False):
        if len(proxies_list) < num_of_accounts_to_generate:
            print(f"[!] Warning: Only {len(proxies_list)} proxies available for {num_of_accounts_to_generate} accounts")
            print(f"[!] Some accounts will be created without proxies")

    print("[*] Starting account generation...\n")

    # Process accounts in batches of 20
    batch_size = 20
    all_results = []

    for batch_start in range(0, num_of_accounts_to_generate, batch_size):
        batch_end = min(batch_start + batch_size, num_of_accounts_to_generate)
        batch_num = (batch_start // batch_size) + 1
        total_batches = (num_of_accounts_to_generate + batch_size - 1) // batch_size

        print(f"\n{'='*60}")
        print(f"[*] Processing Batch {batch_num}/{total_batches} (Accounts {batch_start + 1}-{batch_end})")
        print(f"{'='*60}\n")

        # Create tasks for this batch
        tasks = [
            process_single_hotmail_account(config, idx, num_of_accounts_to_generate, proxies_list, hotmail_accounts)
            for idx in range(batch_start + 1, batch_end + 1)
        ]

        print(f"[*] Running {len(tasks)} account creation tasks in parallel for this batch...")
        batch_results = await asyncio.gather(*tasks, return_exceptions=True)
        all_results.extend(batch_results)

        print(f"\n[✓] Batch {batch_num}/{total_batches} completed")
        print(f"[*] {len([r for r in batch_results if isinstance(r, dict) and r.get('success')])} successful in this batch")
    
    successful_accounts = [r['email'] for r in all_results if isinstance(r, dict) and r.get('success')]
    failed_accounts = [f"{r.get('email', 'N/A')} ({r.get('error', 'Unknown error')})" for r in all_results if isinstance(r, dict) and not r.get('success')]
    
    # Summary
    print(f"\n{'='*60}")
    print("[*] Account Generation Summary")
    print(f"{'='*60}")
    print(f"[✓] Successful: {len(successful_accounts)}")
    print(f"[✗] Failed: {len(failed_accounts)}")
    
    if successful_accounts:
        print("\n[✓] Successfully created accounts:")
        for acc in successful_accounts:
            print(f"  - {acc}")
    
    if failed_accounts:
        print("\n[✗] Failed accounts:")
        for acc in failed_accounts:
            print(f"  - {acc}")

if __name__ == '__main__':
    asyncio.run(main())