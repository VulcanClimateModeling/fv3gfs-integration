from typing import Iterable, Mapping, Union

from .constants import (
    X_DIM,
    X_INTERFACE_DIM,
    Y_DIM,
    Y_INTERFACE_DIM,
    Z_DIM,
    Z_INTERFACE_DIM,
    Z_SOIL_DIM,
)


RestartProperties = Mapping[str, Mapping[str, Union[str, Iterable[str]]]]
RESTART_PROPERTIES: RestartProperties = {
    "cx": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "cx",
        "units": "",
        "long_name": "accumulated_x_courant_number",
    },
    "mfx": {
        "dims": [Z_DIM, Y_DIM, X_INTERFACE_DIM],
        "restart_name": "mfx",
        "units": "unknown",
        "long_name": "accumulated_x_mass_flux",
    },
    "cy": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "cy",
        "units": "unknown",
        "long_name": "accumulated_y_courant_number",
    },
    "mfy": {
        "dims": [Z_DIM, Y_INTERFACE_DIM, X_DIM],
        "restart_name": "mfy",
        "units": "unknown",
        "long_name": "accumulated_y_mass_flux",
    },
    "pt": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "T",
        "units": "degK",
        "long_name": "air_temperature",
    },
    "gt0": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "gt0",
        "units": "K",
        "long_name": "air_temperature_after_physics", 
    },
    "t2m": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "t2m",
        "units": "degK",
        "long_name": "air_temperature_at_2m", 
    },
    "area": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "area",
        "units": "m^2",
        "long_name": "area_of_grid_cell", 
    },
    "ak": {
        "dims": [Z_INTERFACE_DIM],
        "restart_name": "ak",
        "units": "Pa",
        "long_name": "atmosphere_hybrid_a_coordinate",
    },
    "bk": {
        "dims": [Z_INTERFACE_DIM],
        "restart_name": "bk",
        "units": "",
        "long_name": "atmosphere_hybrid_b_coordinate",
    },
    "canopy": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "canopy",
        "units": "unknown",
        "long_name": "canopy_water",
    },
    "sfcflw": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "dnfx0",
        "restart_name": "sfcflw",
        "units": "W/m^2",
        "long_name": "clear_sky_downward_longwave_flux_at_surface",
    },
    "sfcfsw": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "dnfx0",
        "restart_name": "sfcfsw",
        "units": "W/m^2",
        "long_name": "clear_sky_downward_shortwave_flux_at_surface",
    },
    "sfcflw": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "upfx0",
        "restart_name": "sfcflw",
        "units": "W/m^2",
        "long_name": "clear_sky_upward_longwave_flux_at_surface",
    },
    "topflw": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "upfx0",
        "restart_name": "topflw",
        "units": "W/m^2",
        "long_name": "clear_sky_upward_longwave_flux_at_top_of_atmosphere",
    },
    "sfcfsw": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "upfx0",
        "restart_name": "sfcfsw",
        "units": "W/m^2",
        "long_name": "clear_sky_upward_shortwave_flux_at_surface",
    },
    "topfsw": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "upfx0",
        "restart_name": "topfsw",
        "units": "W/m^2",
        "long_name": "clear_sky_upward_shortwave_flux_at_top_of_atmosphere",
    },
    "cvb": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "cvb",
        "units": "Pa",
        "long_name": "convective_cloud_bottom_pressure",
    },
    "cv": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "cv",
        "units": "",
        "long_name": "convective_cloud_fraction",
    },
    "cvt": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "cvt",
        "units": "Pa",
        "long_name": "convective_cloud_top_pressure",
    },
    "tg3": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "tg3",
        "units": "degK",
        "long_name": "deep_soil_temperature",
    },
    "diss_est": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "diss_est",
        "units": "unknown",
        "long_name": "dissipation_estimate_from_heat_source",
    },
    "ua": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "ua",
        "units": "m/s",
        "long_name": "eastward_wind",
    },
    "gu0": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "gu0",
        "units": "m/s",
        "long_name": "eastward_wind_after_physics",
    },
    "u_srf": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "u_srf",
        "units": "m/s",
        "long_name": "eastward_wind_at_surface",
    },
    "ffhh": {
        "description": "used in PBL scheme",
        "dims": [Y_DIM, X_DIM],
        "restart_name": "ffhh",
        "units": "unknown",
        "long_name": "fh_parameter",
    },
    "f10m": {
        "description": "Ratio of sigma level 1 wind and 10m wind",
        "dims": [Y_DIM, X_DIM],
        "restart_name": "f10m",
        "units": "unknown",
        "long_name": "fm_at_10m",
    },
    "ffmm": {
        "description": "used in PBL scheme",
        "dims": [Y_DIM, X_DIM],
        "restart_name": "ffmm",
        "units": "unknown",
        "long_name": "fm_parameter",
    },
    "facsf": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "facsf",
        "units": "",
        "long_name": "fractional_coverage_with_strong_cosz_dependency",
    },
    "facwf": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "facwf",
        "units": "",
        "long_name": "fractional_coverage_with_weak_cosz_dependency",
    },
    "uustar": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "uustar",
        "units": "m/s",
        "long_name": "friction_velocity",
    },
    "fice": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "fice",
        "units": "",
        "long_name": "ice_fraction_over_open_water",
    },
    "pe": {
        "dims": [Y_DIM, Z_INTERFACE_DIM, X_DIM],
        "restart_name": "pe",
        "units": "Pa",
        "long_name": "interface_pressure",
    },
    "pk": {
        "dims": [Z_INTERFACE_DIM, Y_DIM, X_DIM],
        "restart_name": "pk",
        "units": "unknown",
        "long_name": "interface_pressure_raised_to_power_of_kappa",
    },
    "slmsk": {
        "description": "sea=0, land=1, sea-ice=2",
        "dims": [Y_DIM, X_DIM],
        "restart_name": "slmsk",
        "units": "",
        "long_name": "land_sea_mask",
    },
    "dqsfci": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "dqsfci",
        "units": "W/m^2",
        "long_name": "latent_heat_flux",
    },
    "xlat": {"dims": [Y_DIM, X_DIM], "restart_name": "xlat", "units": "radians", "long_name": "latitude",},
    "pkz": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "pkz",
        "units": "unknown",
        "long_name": "layer_mean_pressure_raised_to_power_of_kappa",
    },
    "slc": {
        "dims": [Z_SOIL_DIM, Y_DIM, X_DIM],
        "restart_name": "slc",
        "units": "unknown",
        "long_name": "liquid_soil_moisture",
    },
    "peln": {
        "dims": [Y_DIM, Z_INTERFACE_DIM, X_DIM],
        "restart_name": "peln",
        "units": "ln(Pa)",
        "long_name": "logarithm_of_interface_pressure",
    },
    "xlon": {"dims": [Y_DIM, X_DIM], "restart_name": "xlon", "units": "radians", "long_name": "longitude",},
    "shdmax": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "shdmax",
        "units": "",
        "long_name": "maximum_fractional_coverage_of_green_vegetation",
    },
    "snoalb": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "snoalb",
        "units": "",
        "long_name": "maximum_snow_albedo_in_fraction",
    },
    "coszen": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "coszen",
        "units": "",
        "long_name": "mean_cos_zenith_angle",
    },
    "alnsf": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "alnsf",
        "units": "",
        "long_name": "mean_near_infrared_albedo_with_strong_cosz_dependency",
    },
    "alnwf": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "alnwf",
        "units": "",
        "long_name": "mean_near_infrared_albedo_with_weak_cosz_dependency",
    },
    "alvsf": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "alvsf",
        "units": "",
        "long_name": "mean_visible_albedo_with_strong_cosz_dependency",
    },
    "alvwf": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "alvwf",
        "units": "",
        "long_name": "mean_visible_albedo_with_weak_cosz_dependency",
    },
    "shdmin": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "shdmin",
        "units": "",
        "long_name": "minimum_fractional_coverage_of_green_vegetation",
    },
    "va": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "va",
        "units": "m/s",
        "long_name":"northward_wind",
    },
    "gv0": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "gv0",
        "units": "m/s",
        "long_name": "northward_wind_after_physics",
    },
    "v_srf": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "v_srf",
        "units": "m/s",
        "long_name": "northward_wind_at_surface",
    },
    "delp": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "delp",
        "units": "Pa",
        "long_name": "pressure_thickness_of_atmospheric_layer",
    },
    "hice": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "hice",
        "units": "unknown",
        "long_name": "sea_ice_thickness",
    },
    "dtsfci": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "dtsfci",
        "units": "W/m^2",
        "long_time": "sensible_heat_flux",
    },
    "sncovr": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "sncovr",
        "units": "",
        "long_name": "snow_cover_in_fraction",
    },
    "snwdph": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "snwdph",
        "units": "mm",
        "long_name": "snow_depth_water_equivalent",
    },
    "srflag": {
        "description": "snow/rain flag for precipitation",
        "dims": [Y_DIM, X_DIM],
        "restart_name": "srflag",
        "units": "",
        "long_name": "snow_rain_flag",
    },
    "stc": {
        "dims": [Z_SOIL_DIM, Y_DIM, X_DIM],
        "restart_name": "stc",
        "units": "degK",
        "long_name": "soil_temperature",
    },
    "stype": {"dims": [Y_DIM, X_DIM], "restart_name": "stype", "units": "", "long_name": "soil_type",},
    "q2m": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "q2m",
        "units": "kg/kg",
        "long_name": "specific_humidity_at_2m",
    },
    "phis": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "phis",
        "units": "m^2 s^-2",
        "long_name": "surface_geopotential",
    },
    "surface_pressure": {"dims": [Y_DIM, X_DIM], "restart_name": "ps", "units": "Pa"},
    "surface_roughness": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "zorl",
        "units": "cm",
    },
    "surface_slope_type": {
        "description": "used in land surface model",
        "dims": [Y_DIM, X_DIM],
        "restart_name": "slope",
        "units": "",
    },
    "surface_temperature": {
        "description": "surface skin temperature",
        "dims": [Y_DIM, X_DIM],
        "restart_name": "tsea",
        "units": "degK",
    },
    "surface_temperature_over_ice_fraction": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "tisfc",
        "units": "degK",
    },
    "total_condensate_mixing_ratio": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "q_con",
        "units": "kg/kg",
    },
    "total_precipitation": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "tprcp",
        "units": "m",
    },
    "total_sky_downward_longwave_flux_at_surface": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "dnfxc",
        "restart_name": "sfcflw",
        "units": "W/m^2",
    },
    "total_sky_downward_shortwave_flux_at_surface": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "dnfxc",
        "restart_name": "sfcfsw",
        "units": "W/m^2",
    },
    "total_sky_downward_shortwave_flux_at_top_of_atmosphere": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "dnfxc",
        "restart_name": "topfsw",
        "units": "W/m^2",
    },
    "total_sky_upward_longwave_flux_at_surface": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "upfxc",
        "restart_name": "sfcflw",
        "units": "W/m^2",
    },
    "total_sky_upward_longwave_flux_at_top_of_atmosphere": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "upfxc",
        "restart_name": "topflw",
        "units": "W/m^2",
    },
    "total_sky_upward_shortwave_flux_at_surface": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "upfxc",
        "restart_name": "sfcfsw",
        "units": "W/m^2",
    },
    "total_sky_upward_shortwave_flux_at_top_of_atmosphere": {
        "dims": [Y_DIM, X_DIM],
        "fortran_subname": "upfxc",
        "restart_name": "topfsw",
        "units": "W/m^2",
    },
    "total_soil_moisture": {
        "dims": [Z_SOIL_DIM, Y_DIM, X_DIM],
        "restart_name": "smc",
        "units": "unknown",
    },
    "vegetation_fraction": {
        "dims": [Y_DIM, X_DIM],
        "restart_name": "vfrac",
        "units": "",
    },
    "vegetation_type": {"dims": [Y_DIM, X_DIM], "restart_name": "vtype", "units": ""},
    "vertical_pressure_velocity": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "omga",
        "units": "Pa/s",
    },
    "vertical_thickness_of_atmospheric_layer": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "DZ",
        "units": "m",
    },
    "vertical_wind": {
        "dims": [Z_DIM, Y_DIM, X_DIM],
        "restart_name": "W",
        "units": "m/s",
    },
    "water_equivalent_of_accumulated_snow_depth": {
        "description": "weasd in Fortran code, over land and sea ice only",
        "dims": [Y_DIM, X_DIM],
        "restart_name": "sheleg",
        "units": "kg/m^2",
    },
    "x_wind": {
        "dims": [Z_DIM, Y_INTERFACE_DIM, X_DIM],
        "restart_name": "u",
        "units": "m/s",
    },
    "x_wind_on_c_grid": {
        "dims": [Z_DIM, Y_DIM, X_INTERFACE_DIM],
        "restart_name": "uc",
        "units": "m/s",
    },
    "y_wind": {
        "dims": [Z_DIM, Y_DIM, X_INTERFACE_DIM],
        "restart_name": "v",
        "units": "m/s",
    },
    "y_wind_on_c_grid": {
        "dims": [Z_DIM, Y_INTERFACE_DIM, X_DIM],
        "restart_name": "vc",
        "units": "m/s",
    },
}
