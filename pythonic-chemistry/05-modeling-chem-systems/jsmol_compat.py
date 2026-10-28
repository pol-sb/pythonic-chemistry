"""Compatibility layer for the notebook's original JSmolView API.

The course notebooks were written for ``jupyter-jsmol``, whose JupyterLab
frontend does not load reliably in JupyterLab 4 / Binder. This module provides
the same small API used by the notebooks on top of ``py3Dmol``, which renders
a static, interactive 3D viewer without a custom widget extension.
"""

from io import StringIO

import ase.io
import py3Dmol


class JsmolView:
    """Minimal drop-in replacement for ``jupyter_jsmol.JsmolView``."""

    def __init__(self, view):
        self._view = view

    @classmethod
    def from_file(cls, source, *args, **kwargs):
        if hasattr(source, "read"):
            atoms = ase.io.read(source, format="xyz")
        else:
            atoms = ase.io.read(source)

        buffer = StringIO()
        ase.io.write(buffer, atoms, format="xyz")

        view = py3Dmol.view(width=600, height=400)
        view.addModel(buffer.getvalue(), "xyz")
        view.setStyle({"stick": {}, "sphere": {"scale": 0.3}})
        view.setBackgroundColor("white")
        view.zoomTo()
        return cls(view)

    def script(self, command):
        command = command.strip()
        if command.startswith("background"):
            color = command.split()[-1]
            self._view.setBackgroundColor(color)
            self._view.update()

    def close(self):
        # py3Dmol output is static and disappears with the notebook output.
        pass

    def _ipython_display_(self, **kwargs):
        self._view.show()

    def _repr_html_(self):
        return self._view._make_html()
