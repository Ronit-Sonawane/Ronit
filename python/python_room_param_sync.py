import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

# Process input MEP elements passed from Dynamo
elements = IN[0] if isinstance(IN[0], list) else [IN[0]]
updated_count = 0

TransactionManager.Instance.EnsureInTransaction(doc)

for item in elements:
    revit_elem = UnwrapElement(item)
    if hasattr(revit_elem, "Space") and revit_elem.Space:
        space_name = revit_elem.Space.Name
        param = revit_elem.LookupParameter("Comments")
        if param and not param.IsReadOnly:
            param.Set(f"Located in Space: {space_name}")
            updated_count += 1

TransactionManager.Instance.TransactionTaskDone()

OUT = f"Successfully updated parameters for {updated_count} elements."
