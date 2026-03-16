from enum import Enum


class ColorConversionStrategyEnum(str, Enum):
    CMYK = "CMYK"
    GRAY = "Gray"
    LEAVECOLORUNCHANGED = "LeaveColorUnchanged"
    RGB = "RGB"
    USEDEVICEINDEPENDENTCOLOR = "UseDeviceIndependentColor"

    def __str__(self) -> str:
        return str(self.value)
