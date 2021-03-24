from dataclasses import dataclass

@dataclass
class coordinates(object):
    """data class for image object coordinates"""
    x: int
    y: int
    w: int
    h: int
