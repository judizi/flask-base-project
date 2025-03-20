import importlib
import pkgutil

from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint('blueprint', __name__, url_prefix='/')

api = Api(blueprint, title="REST API", version="1.0")


def list_all_modules(base_package_name):
    modules = []
    packages = []

    base_package = importlib.import_module(base_package_name)
    if hasattr(base_package, "__path__"):
        for _, module_name, is_pkg in pkgutil.walk_packages(base_package.__path__, base_package_name + "."):
            if is_pkg:
                if module_name != base_package_name:
                    packages.append(module_name)
            else:
                if ".".join(module_name.split(".")[:-1]) not in packages:
                    modules.append(module_name)

    return modules, packages

def import_modules(package_name):
    ns_lib = importlib.import_module(package_name)
    if hasattr(ns_lib, "path") and ns_lib.path != "":
        api.add_namespace(ns_lib.ns, path=ns_lib.path)

modules, packages = list_all_modules(__name__)
while len(packages) > 0:
    for idx, package in enumerate(packages):
        sub_modules, sub_packages = list_all_modules(package)
        packages.pop(idx)
        modules += sub_modules
        packages += sub_packages

modules = list(dict.fromkeys(modules))
for module in modules:
    import_modules(module)
