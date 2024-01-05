#!/usr/bin/env python3
'''This is only a very simple authentication example which stores session IDs in memory and does not do any password hashing.

Please see the `OAuth2 example at FastAPI <https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/>`_  or
use the great `Authlib package <https://docs.authlib.org/en/v0.13/client/starlette.html#using-fastapi>`_ to implement a real authentication system.

Here we just demonstrate the NiceGUI integration.
'''

import os
import uuid
from typing import Dict

from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

from nicegui import app, ui

import plugins
import sections

# put your your own secret key in an environment variable MY_SECRET_KEY
app.add_middleware(SessionMiddleware, secret_key=os.environ.get('MY_SECRET_KEY', ''))

# in reality users and session_info would be persistent (e.g. database, file, ...) and passwords obviously hashed
users = [('system', 'sys'), ('user2', 'pass2')]
session_info: Dict[str, Dict] = {}


def is_authenticated(request: Request) -> bool:
    return session_info.get(request.session.get('id'), {}).get('authenticated', False)


@ui.page('/')
def main_page(request: Request) -> None:
    if not is_authenticated(request):
        return RedirectResponse('/login')
    session = session_info[request.session['id']]

    with ui.header().classes(replace='flex items-center justify-between p-6 bg-gray-900 text-white') as header:
        with ui.row():
            with ui.tabs().classes('flex space-x-4'):
                for names in sections.list:
                    ui.tab(names)

            ui.label(f'Hello {session["username"]}!').classes('text-2xl')
            ui.button('', on_click=lambda: ui.open('/logout')).props('outline round color-red icon-logout')

    with ui.footer(value=False).classes('bg-gray-800 text-white p-4'):
        ui.label('Footer')

    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=lambda: ui.notify('Contact Support clicked', color='primary')).props('fab icon-contact_support')

    with ui.tab_panels().classes('p-6'):
        for name in sections.list:
            with ui.tab_panel(name):
                list_plugins = plugins.get_section_plugins(name)
                with ui.row():
                    with ui.tabs().classes('flex space-y-4 flex-col'):
                        for sub_name in list_plugins:
                            ui.tab(sub_name, icon='home')

                    with ui.tab_panels().classes('flex flex-1 space-y-4'):
                        for sub_name in list_plugins:
                            with ui.tab_panel(sub_name):
                                ui.label(f'This is the {sub_name} tab ')
                                plugins.get_content(name, sub_name)


@ui.page('/login')
def login(request: Request) -> None:
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        if (username.value, password.value) in users:
            session_info[request.session['id']] = {'username': username.value, 'authenticated': True}
            ui.open('/')
        else:
            ui.notify('Wrong username or password', color='negative')

    if is_authenticated(request):
        return RedirectResponse('/')
    request.session['id'] = str(uuid.uuid4())  # NOTE this stores a new session ID in the cookie of the client
    with ui.card().classes('max-w-md mx-auto p-6 bg-white rounded-lg shadow-md'):
        username = ui.input('Username').on('keydown.enter', try_login).classes('mb-4')
        password = ui.input('Password').props('type=password').on('keydown.enter', try_login).classes('mb-4')
        ui.button('Log in', on_click=try_login).props('bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline')


@ui.page('/logout')
def logout(request: Request) -> None:
    if is_authenticated(request):
        session_info.pop(request.session['id'])
        request.session['id'] = None
        return RedirectResponse('/login')
    return RedirectResponse('/')

ui.run()
