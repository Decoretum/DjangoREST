from rest_framework import permissions

class IsStaffEditor(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions()) #returns set() which is none
        if request.user.is_staff:
            if user.has_perm("products.view_product"): #Appname.action_modelname
                return True
            if user.has_perm("products.add_product"):
                return True
            return False
        
        return False
        
class IsStaff(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False