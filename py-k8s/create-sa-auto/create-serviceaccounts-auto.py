# For the script to work you need kubernetes (library)
# pip install kubernetes

from kubernetes import client, config

# Load the Kubernetes configuration from the default location
config.load_kube_config()

# Create a Kubernetes API client
v1 = client.CoreV1Api()
rbac_api = client.RbacAuthorizationV1Api()

# Define the namespace and user to create
namespace = "default"   # namespace must exist!
username = ""
with open('./users.txt', 'r') as users:
    for line in users.readlines():
        username = line.strip()


        # Create a Kubernetes users
        user = client.V1ObjectMeta(name=username)

        # Create the Kubernetes user in the specified namespace
        v1.create_namespaced_service_account(namespace, client.V1ServiceAccount(metadata=user))

        # Define the role binding to create
        role_binding = client.V1RoleBinding(
            metadata=client.V1ObjectMeta(name=f"{username}-role-binding"),
            role_ref=client.V1RoleRef(api_group="rbac.authorization.k8s.io", kind="ClusterRole", name="view"),
            subjects=[client.V1Subject(api_group="rbac.authorization.k8s.io", kind="User", name=username)]
        )

        # Create the role binding in the specified namespace
        rbac_api.create_namespaced_role_binding(namespace, role_binding)


