class SolidOptions(object,IDisposable):
 """
 A class containing optional information to control the properties of the Solid generated by the GeometryCreationUtilities routines.
 
 SolidOptions(materialId: ElementId,graphicsStyleId: ElementId)
 """
 def Dispose(self):
  """ Dispose(self: SolidOptions) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: SolidOptions,disposing: bool) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,materialId,graphicsStyleId):
  """ __new__(cls: type,materialId: ElementId,graphicsStyleId: ElementId) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 GraphicsStyleId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines the graphics style id for the Solid.

Get: GraphicsStyleId(self: SolidOptions) -> ElementId

Set: GraphicsStyleId(self: SolidOptions)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SolidOptions) -> bool

"""

 MaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines the material id for the Solid.

Get: MaterialId(self: SolidOptions) -> ElementId

Set: MaterialId(self: SolidOptions)=value
"""

