logo_path = "/esa/images/logo.png"
exit_path = "/esa/images/exit.png"
splashscreen_path = "/esa/images/splashscreen.png"

lock_files = ['/esa/lock/passwd.lck', '/esa/lock/shadow.lck']
esa_lock = '/esa/lock/esa.lck'

cmd_useradmin_path = "/esa/scripts/user/useradmin"

cmd_rich_limit_ftp = '/esa/scripts/firewall/rich_rules/connection_limit_ftp.sh'
cmd_rich_list = '/esa/scripts/firewall/rich_rules/list_rich_rules.sh'
cmd_rich_port_forward = '/esa/scripts/firewall/rich_rules/port_forwading.sh'
cmd_rich_port_range = '/esa/scripts/firewall/rich_rules/port_range_of_subnet.sh'
cmd_rich_masquerade = '/esa/scripts/firewall/rich_rules/masquerade_a_source.sh'
cmd_rich_reject_traffic = '/esa/scripts/firewall/rich_rules/reject_all_traffic_from_source.sh'

cmd_zone_add_service = '/esa/scripts/firewall/zones/add_service.sh'
cmd_zone_add_source = '/esa/scripts/firewall/zones/add_source.sh'
cmd_zone_get_default_zone = '/esa/scripts/firewall/zones/get_default_zone.sh'
cmd_zone_get_services = '/esa/scripts/firewall/zones/get_services.sh'
cmd_zone_list_all = '/esa/scripts/firewall/zones/list_all.sh'
cmd_zone_list_zones = '/esa/scripts/firewall/zones/list_all_zones.sh'
cmd_zone_remove_service = '/esa/scripts/firewall/zones/remove_service.sh'
cmd_zone_remove_source = '/esa/scripts/firewall/zones/remove_source.sh'
cmd_zone_set_default_zone = '/esa/scripts/firewall/zones/set_default_zone.sh'

cmd_get_acl = '/esa/scripts/acl/get_acl.sh'
cmd_remove_acl = '/esa/scripts/acl/remove_acl.sh'
cmd_set_acl = '/esa/scripts/acl/set_acl.sh'
cmd_set_default_directory_acl = '/esa/scripts/acl/set_default_directory_acl.sh'
cmd_set_from_existing_file = '/esa/scripts/acl/set_from_existing_file.sh'

cmd_passwd = '/usr/bin/passwd'

error_log = "/tmp/error.log"
output_log = "/tmp/output.log"
user_log = '/tmp/user.log'

title_acl = 'Access Control List'
title_get_acl = 'Get ACL data from file'
title_remove_acl = 'Remove ACL from file'
title_set_acl = 'Set ACL of a file'
title_set_default_dir_acl = 'Set ACL default directory'
title_set_from_existing_file = 'Set ACL from existing file'

title_rich_rules = 'Rich Rules'
title_rich_limit_ftp = 'Limit FTP connections'
title_rich_list = 'List all rich rules'
title_rich_port_forwading = 'Port Forwading'
title_rich_masquerade = 'Masquerade a source'
title_rich_port_range = 'Port Range of subnet'
title_rich_reject_traffic = 'Reject all traffic from source'

title_zone_rules = 'Zone Rules'
title_zone_add_service = 'Add Service'
title_zone_add_source = 'Add Source'
title_zone_get_default_zone = 'Get default Zone'
title_zone_get_services = 'Get Services'
title_zone_list_all = 'List All'
title_zone_list_zones = 'List all zones'
title_zone_remove_service = 'Remove Service'
title_zone_remove_source = 'Remove Source'
title_zone_set_default_zone = 'Set default Zone'