from azure.servicebus import ServiceBusService

key_name = 'RootManageSharedAccessKey' # SharedAccessKeyName from Azure portal
key_value = 'zUCBEyvkIml8p7ClqSibF4yLkkNwWU2dyfotP0vcMTY=' # SharedAccessKey from Azure portal

sbs = ServiceBusService('ArrowTest', shared_access_key_name=key_name,
                        shared_access_key_value=key_value)

msg = sbs.receive_queue_message('inbound_encounter')

print(msg)
