import os
from kubernetes import client, config, watch
from plyer import notification

# Load the kubeconfig file
config.load_kube_config()

# Create an instance of the Kubernetes API client
api_instance = client.CoreV1Api()

# Use the watch function to stream updates of pods in the cluster
w = watch.Watch()

for event in w.stream(api_instance.list_pod_for_all_namespaces):
    
    # Print the type and name of the event
    print("Event: %s %s" % (event['type'], event['object'].metadata.name))
    
    # Filter events related to failed pods
    if 'failed' in event['object'].status.phase:
        
        # Print the name and reason of the failed pod
        print("Pod: %s - Reason: %s" % (event['object'].metadata.name, event['object'].status.reason))
        
        # Send OS notification
        notification.notify(
            title='Failed Pod',
            message=f'Pod {event["object"].metadata.name} has failed. Reason: {event["object"].status.reason}',
            timeout=10
        )    
    else:
        
        # Check the status of the containers inside the pod
        if event['object'].status.container_statuses is not None:
            for container_status in event['object'].status.container_statuses:
                if container_status.state.waiting is not None and 'ErrImagePull' in container_status.state.waiting.reason:
                    print(f"Pod: {event['object'].metadata.name} - Reason: {container_status.state.waiting.reason}")
                    notification.notify(
                        title='Failed Pod',
                        message=f'Pod {event["object"].metadata.name} has failed. Reason: {container_status.state.waiting.reason}',
                        timeout=10
                    )
                elif container_status.state.terminated is not None and container_status.state.terminated.exit_code != 0:
                    print(f"Pod: {event['object'].metadata.name} - Reason: {container_status.state.terminated.reason}")
                    notification.notify(
                        title='Failed Pod',
                        message=f'Pod {event["object"].metadata.name} has failed. Reason: {container_status.state.terminated.reason}',
                        timeout=10
                    )
