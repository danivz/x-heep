from .cpu import CPU


class cv32e40p(CPU):
    """
    Represents the CV32E40P CPU configuration with optional parameters.
    """

    def __init__(
        self,
        rv32f=None,
        rv32f_addmul_lat=None,
        rv32f_compconv_lat=None,
        rv32zfinx=None,
        rv32xcv=None,
        rv32xcvelw=None,
        num_mhpmcounters=None,
    ):
        super().__init__("cv32e40p")

        if rv32f is not None:
            if isinstance(rv32f, str):
                if rv32f.lower() not in ("true", "false", "1", "0"):
                    raise ValueError(
                        f"rv32f must be 0, 1, True, or False, got '{rv32f}'"
                    )
                rv32f = rv32f.lower() in ("true", "1")

            if rv32f not in (0, 1, True, False):
                raise ValueError(f"rv32f must be 0, 1, True, or False, got '{rv32f}'")

            self.params["rv32f"] = bool(rv32f)

        if rv32f_addmul_lat is not None:
            if isinstance(rv32f_addmul_lat, str):
                try:
                    rv32f_addmul_lat = int(rv32f_addmul_lat.lower())
                except:
                    raise ValueError(
                        f"rv32f_addmul_lat must be a number, got '{rv32f_addmul_lat}'"
                    )

            if rv32f_addmul_lat < 0:
                raise ValueError(
                    f"rv32f_addmul_lat must be a positive number, got '{rv32f_addmul_lat}'"
                )

            self.params["rv32f_addmul_lat"] = rv32f_addmul_lat

        if rv32f_compconv_lat is not None:
            if isinstance(rv32f_compconv_lat, str):
                try:
                    rv32f_compconv_lat = int(rv32f_compconv_lat.lower())
                except:
                    raise ValueError(
                        f"rv32f_compconv_lat must be a number, got '{rv32f_compconv_lat}'"
                    )

            if rv32f_compconv_lat < 0:
                raise ValueError(
                    f"rv32f_compconv_lat must be a positive number, got '{rv32f_compconv_lat}'"
                )

            self.params["rv32f_compconv_lat"] = rv32f_compconv_lat

        if rv32zfinx is not None:
            if rv32f is None or rv32f in (0, False):
                raise ValueError("rv32zfinx requires rv32f enabled")
            if isinstance(rv32zfinx, str):
                if rv32zfinx.lower() not in ("true", "false", "1", "0"):
                    raise ValueError(
                        f"rv32zfinx must be 0, 1, True, or False, got '{rv32zfinx}'"
                    )
                rv32zfinx = rv32zfinx.lower() in ("true", "1")

            if rv32zfinx not in (0, 1, True, False):
                raise ValueError(
                    f"rv32zfinx must be 0, 1, True, or False, got '{rv32zfinx}'"
                )

            self.params["rv32zfinx"] = bool(rv32zfinx)

        if rv32xcv is not None:
            if isinstance(rv32xcv, str):
                if rv32xcv.lower() not in ("true", "false", "1", "0"):
                    raise ValueError(
                        f"rv32xcv must be 0, 1, True, or False, got '{rv32xcv}'"
                    )
                rv32xcv = rv32xcv.lower() in ("true", "1")

            if rv32xcv not in (0, 1, True, False):
                raise ValueError(
                    f"rv32xcv must be 0, 1, True, or False, got '{rv32xcv}'"
                )

            self.params["rv32xcv"] = bool(rv32xcv)

        if rv32xcvelw is not None:
            if isinstance(rv32xcvelw, str):
                if rv32xcvelw.lower() not in ("true", "false", "1", "0"):
                    raise ValueError(
                        f"rv32xcvelw must be 0, 1, True, or False, got '{rv32xcvelw}'"
                    )
                rv32xcvelw = rv32xcvelw.lower() in ("true", "1")

            if rv32xcvelw not in (0, 1, True, False):
                raise ValueError(
                    f"rv32xcvelw must be 0, 1, True, or False, got '{rv32xcvelw}'"
                )

            self.params["rv32xcvelw"] = bool(rv32xcvelw)

        if num_mhpmcounters is not None:
            if isinstance(num_mhpmcounters, str):
                try:
                    num_mhpmcounters = int(num_mhpmcounters.lower())
                except:
                    raise ValueError(
                        f"num_mhpmcounters must be a number, got '{num_mhpmcounters}'"
                    )

            if num_mhpmcounters < 0:
                raise ValueError(
                    f"num_mhpmcounters must be a positive number, got '{num_mhpmcounters}'"
                )

            self.params["num_mhpmcounters"] = num_mhpmcounters

    def get_sv_str(self, param_name: str) -> str:
        """
        Get the string representation of the param_name parameter to be used in the SystemVerilog templates.
        :param param_name: Name of the parameter.
        :return: String representation of the parameter for SystemVerilog or an empty string if not defined.
        """
        if not self.is_defined(param_name):
            return ""

        value = self.params[param_name]
        if param_name == "rv32f":
            return "1" if value else "0"
        elif param_name == "rv32zfinx":
            return "1" if value else "0"
        elif param_name == "rv32xcv":
            return "1" if value else "0"
        elif param_name == "rv32xcvelw":
            return "1" if value else "0"
        else:
            return str(value)
