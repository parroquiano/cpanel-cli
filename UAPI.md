`/usr/local/cpanel/bin/uapi`

- [ ] AccountEnhancements::has_enhancement
- [ ] AccountEnhancements::list
- [ ] AuditLog::get_api_log
- [x] Backup::fullbackup_to_ftp
- [x] Backup::fullbackup_to_homedir
- [-] Backup::fullbackup_to_scp_with_key
- [x] Backup::fullbackup_to_scp_with_password
- [x] Backup::list_backups
- [-] Backup::restore_databases
- [-] Backup::restore_email_filters
- [-] Backup::restore_email_forwarders
- [x] Backup::restore_files
- [x] Bandwidth::get_enabled_protocols
- [x] Bandwidth::get_retention_periods
- [ ] Bandwidth::query
- [ ] Batch::strict
- [x] BlockIP::add_ip
- [x] BlockIP::remove_ip
- [ ] BoxTrapper::blacklist_messages
- [ ] BoxTrapper::delete_messages
- [ ] BoxTrapper::deliver_messages
- [ ] BoxTrapper::get_allowlist
- [ ] BoxTrapper::get_blocklist
- [ ] BoxTrapper::get_configuration
- [ ] BoxTrapper::get_email_template
- [ ] BoxTrapper::get_forwarders
- [ ] BoxTrapper::get_ignorelist
- [ ] BoxTrapper::get_log
- [ ] BoxTrapper::get_message
- [ ] BoxTrapper::get_status
- [ ] BoxTrapper::ignore_messages
- [ ] BoxTrapper::list_email_templates
- [ ] BoxTrapper::list_queued_messages
- [ ] BoxTrapper::process_messages
- [ ] BoxTrapper::reset_email_template
- [ ] BoxTrapper::save_configuration
- [ ] BoxTrapper::save_email_template
- [ ] BoxTrapper::set_allowlist
- [ ] BoxTrapper::set_blocklist
- [ ] BoxTrapper::set_forwarders
- [ ] BoxTrapper::set_ignorelist
- [ ] BoxTrapper::set_status
- [ ] BoxTrapper::whitelist_messages
- [ ] Branding::get_application_information
- [ ] Branding::get_applications
- [ ] Branding::get_available_applications
- [ ] Branding::get_information_for_applications
- [ ] Branding::include
- [ ] CSVImport::doimport
- [x] CacheBuster::read
- [x] CacheBuster::update
- [ ] Chkservd::get_exim_ports
- [ ] Chkservd::get_exim_ports_ssl
- [ ] Chrome::get_dom
- [ ] ClamScanner::check_disinfection_status
- [ ] ClamScanner::disinfect_files
- [ ] ClamScanner::get_scan_paths
- [ ] ClamScanner::get_scan_status
- [ ] ClamScanner::list_infected_files
- [ ] ClamScanner::start_scan
- [ ] ContactInformation::set_email_addresses
- [ ] ContactInformation::unset_email_addresses
- [ ] Contactus::is_enabled
- [ ] DAV::disable_shared_global_addressbook
- [ ] DAV::enable_shared_global_addressbook
- [ ] DAV::get_calendar_contacts_config
- [ ] DAV::has_shared_global_addressbook
- [ ] DAV::is_ccs_enabled
- [ ] DAV::is_dav_service_enabled
- [ ] DAV::is_horde_enabled
- [ ] DCV::check_domains_via_dns
- [ ] DCV::check_domains_via_http
- [ ] DCV::ensure_domains_can_pass_dcv
- [x] DNS::ensure_domains_reside_only_locally
- [x] DNS::has_local_authority
- [x] DNS::lookup
- [ ] DNS::mass_edit_zone
- [ ] DNS::parse_zone
- [ ] DNS::swap_ip_in_zones
- [ ] DNSSEC::activate_zone_key
- [ ] DNSSEC::add_zone_key
- [ ] DNSSEC::deactivate_zone_key
- [ ] DNSSEC::disable_dnssec
- [ ] DNSSEC::enable_dnssec
- [ ] DNSSEC::export_zone_dnskey
- [ ] DNSSEC::export_zone_key
- [ ] DNSSEC::fetch_ds_records
- [ ] DNSSEC::import_zone_key
- [ ] DNSSEC::remove_zone_key
- [ ] DNSSEC::set_nsec3
- [ ] DNSSEC::unset_nsec3
- [x] DirectoryIndexes::get_indexing
- [x] DirectoryIndexes::list_directories
- [x] DirectoryIndexes::set_indexing
- [x] DirectoryPrivacy::add_user
- [x] DirectoryPrivacy::configure_directory_protection
- [x] DirectoryPrivacy::delete_user
- [x] DirectoryPrivacy::is_directory_protected
- [x] DirectoryPrivacy::list_directories
- [x] DirectoryPrivacy::list_users
- [x] DirectoryProtection::list_directories
- [x] DomainInfo::domains_data
- [x] DomainInfo::list_domains
- [x] DomainInfo::main_domain_builtin_subdomain_aliases
- [x] DomainInfo::single_domain_data
- [x] DynamicDNS::create
- [x] DynamicDNS::delete
- [x] DynamicDNS::list
- [x] DynamicDNS::recreate
- [x] DynamicDNS::set_description
- [ ] EA4::get_php_recommendations
- [ ] EA4::get_recommendations
- [-] Email::account_name
- [x] Email::add_auto_responder
- [x] Email::add_domain_forwarder
- [x] Email::add_forwarder
- [x] Email::add_list
- [x] Email::add_mailman_delegates
- [ ] Email::add_mx
- [ ] Email::add_pop
- [x] Email::add_spam_filter
- [x] Email::browse_mailbox
- [ ] Email::change_mx
- [ ] Email::check_fastmail
- [x] Email::count_auto_responders
- [x] Email::count_filters
- [x] Email::count_forwarders
- [x] Email::count_lists
- [x] Email::count_pops
- [x] Email::delete_auto_responder
- [x] Email::delete_domain_forwarder
- [x] Email::delete_filter
- [x] Email::delete_forwarder
- [ ] Email::delete_held_messages
- [x] Email::delete_list
- [ ] Email::delete_mx
- [ ] Email::delete_pop
- [x] Email::disable_filter
- [ ] Email::disable_mailbox_autocreate
- [x] Email::disable_spam_assassin
- [x] Email::disable_spam_autodelete
- [x] Email::disable_spam_box
- [ ] Email::dispatch_client_settings
- [x] Email::edit_pop_quota
- [x] Email::enable_filter
- [ ] Email::enable_mailbox_autocreate
- [x] Email::enable_spam_assassin
- [x] Email::enable_spam_box
- [ ] Email::fetch_charmaps
- [ ] Email::fts_rescan_mailbox
- [x] Email::generate_mailman_otp
- [x] Email::get_auto_responder
- [ ] Email::get_charsets
- [x] Email::get_client_settings
- [-] Email::get_default_email_quota
- [x] Email::get_default_email_quota_mib
- [x] Email::get_disk_usage
- [x] Email::get_filter
- [ ] Email::get_held_message_count
- [x] Email::get_lists_total_disk_usage
- [ ] Email::get_mailbox_autocreate
- [x] Email::get_mailman_delegates
- [-] Email::get_main_account_disk_usage
- [-] Email::get_main_account_disk_usage_bytes
- [-] Email::get_max_email_quota
- [x] Email::get_max_email_quota_mib
- [x] Email::get_pop_quota
- [x] Email::get_spam_settings
- [x] Email::get_webmail_settings
- [x] Email::has_delegated_mailman_lists
- [ ] Email::has_plaintext_authentication
- [ ] Email::hold_outgoing
- [x] Email::list_auto_responders
- [ ] Email::list_default_address
- [x] Email::list_domain_forwarders
- [x] Email::list_filters
- [x] Email::list_filters_backups
- [x] Email::list_forwarders
- [-] Email::list_forwarders_backups
- [x] Email::list_lists
- [ ] Email::list_mail_domains
- [ ] Email::list_mxs
- [x] Email::list_pops
- [ ] Email::list_pops_with_disk
- [-] Email::list_system_filter_info
- [x] Email::passwd_list
- [ ] Email::passwd_pop
- [ ] Email::release_outgoing
- [x] Email::remove_mailman_delegates
- [x] Email::reorder_filters
- [ ] Email::set_always_accept
- [ ] Email::set_default_address
- [x] Email::set_list_privacy_options
- [ ] Email::set_manual_mx_redirects
- [ ] Email::stats_db_status
- [x] Email::store_filter
- [x] Email::suspend_incoming
- [x] Email::suspend_login
- [x] Email::suspend_outgoing
- [ ] Email::terminate_mailbox_sessions
- [ ] Email::trace_delivery
- [x] Email::trace_filter
- [ ] Email::unset_manual_mx_redirects
- [x] Email::unsuspend_incoming
- [x] Email::unsuspend_login
- [x] Email::unsuspend_outgoing
- [ ] Email::verify_password
- [ ] EmailAuth::disable_dkim
- [ ] EmailAuth::enable_dkim
- [ ] EmailAuth::ensure_dkim_keys_exist
- [ ] EmailAuth::fetch_dkim_private_keys
- [ ] EmailAuth::install_dkim_private_keys
- [ ] EmailAuth::install_spf_records
- [ ] EmailAuth::validate_current_dkims
- [ ] EmailAuth::validate_current_ptrs
- [ ] EmailAuth::validate_current_spfs
- [ ] ExternalAuthentication::add_authn_link
- [ ] ExternalAuthentication::configured_modules
- [ ] ExternalAuthentication::get_authn_links
- [ ] ExternalAuthentication::has_external_auth_modules_configured
- [ ] ExternalAuthentication::remove_authn_link
- [x] Features::get_feature_metadata
- [x] Features::has_feature
- [x] Features::list_features
- [x] Fileman::autocompletedir
- [x] Fileman::empty_trash
- [x] Fileman::get_file_content
- [x] Fileman::get_file_information
- [x] Fileman::list_files
- [x] Fileman::save_file_content
- [-] Fileman::transcode
- [x] Fileman::upload_files
- [x] Ftp::add_ftp
- [x] Ftp::allows_anonymous_ftp
- [x] Ftp::allows_anonymous_ftp_incoming
- [x] Ftp::delete_ftp
- [x] Ftp::ftp_exists
- [x] Ftp::get_ftp_daemon_info
- [x] Ftp::get_port
- [x] Ftp::get_quota
- [x] Ftp::get_welcome_message
- [x] Ftp::kill_session
- [-] Ftp::list_ftp
- [x] Ftp::list_ftp_with_disk
- [x] Ftp::list_sessions
- [x] Ftp::passwd
- [-] Ftp::server_name
- [x] Ftp::set_anonymous_ftp
- [x] Ftp::set_anonymous_ftp_incoming
- [x] Ftp::set_homedir
- [x] Ftp::set_quota
- [x] Ftp::set_welcome_message
- [ ] GPG::delete_keypair
- [ ] GPG::export_public_key
- [ ] GPG::export_secret_key
- [ ] GPG::generate_key
- [ ] GPG::import_key
- [ ] GPG::list_public_keys
- [ ] GPG::list_secret_keys
- [ ] ImageManager::convert_file
- [ ] ImageManager::create_thumbnails
- [ ] ImageManager::get_dimensions
- [ ] ImageManager::resize_image
- [ ] InstallWordpress::capturex
- [ ] InstallWordpress::decode_json
- [ ] InstallWordpress::encode_json
- [ ] InstallWordpress::from_json
- [ ] InstallWordpress::hello
- [ ] InstallWordpress::install_wordpress
- [ ] InstallWordpress::jsonToObj
- [ ] InstallWordpress::objToJson
- [ ] InstallWordpress::to_json
- [ ] Integration::fetch_url
- [ ] KnownHosts::create
- [ ] KnownHosts::delete
- [ ] KnownHosts::update
- [ ] KnownHosts::verify
- [ ] LangPHP::php_get_domain_handler
- [ ] LangPHP::php_get_impacted_domains
- [ ] LangPHP::php_get_installed_versions
- [ ] LangPHP::php_get_system_default_version
- [ ] LangPHP::php_get_vhost_versions
- [ ] LangPHP::php_ini_get_user_basic_directives
- [ ] LangPHP::php_ini_get_user_content
- [ ] LangPHP::php_ini_get_user_paths
- [ ] LangPHP::php_ini_set_user_basic_directives
- [ ] LangPHP::php_ini_set_user_content
- [ ] LangPHP::php_set_vhost_versions
- [ ] LastLogin::get_last_or_current_logged_in_ip
- [x] Locale::get_attributes
- [x] Locale::list_locales
- [x] Locale::set_locale
- [x] LogManager::get_settings
- [x] LogManager::list_archives
- [x] LogManager::set_settings
- [ ] Mailboxes::expunge_mailbox_messages
- [ ] Mailboxes::expunge_messages_for_mailbox_guid
- [ ] Mailboxes::get_mailbox_status_list
- [ ] Mailboxes::has_utf8_mailbox_names
- [ ] Mailboxes::set_utf8_mailbox_names
- [ ] Market::cancel_pending_ssl_certificate
- [ ] Market::create_shopping_cart
- [ ] Market::create_shopping_cart_non_ssl
- [ ] Market::get_all_products
- [ ] Market::get_build_cart_url
- [ ] Market::get_certificate_status_details
- [ ] Market::get_completion_url
- [ ] Market::get_license_info
- [ ] Market::get_login_url
- [ ] Market::get_pending_ssl_certificates
- [ ] Market::get_product_info
- [ ] Market::get_provider_specific_dcv_constraints
- [ ] Market::get_providers_list
- [ ] Market::get_ssl_certificate_if_available
- [ ] Market::process_ssl_pending_queue
- [ ] Market::request_ssl_certificates
- [ ] Market::set_status_of_pending_queue_items
- [ ] Market::set_url_after_checkout
- [ ] Market::validate_login_token
- [ ] Mime::add_handler
- [ ] Mime::add_hotlink
- [ ] Mime::add_mime
- [ ] Mime::add_redirect
- [ ] Mime::delete_handler
- [ ] Mime::delete_hotlink
- [ ] Mime::delete_mime
- [ ] Mime::delete_redirect
- [ ] Mime::get_redirect
- [ ] Mime::list_handlers
- [ ] Mime::list_hotlinks
- [ ] Mime::list_mime
- [ ] Mime::list_redirects
- [ ] Mime::redirect_info
- [ ] ModSecurity::disable_all_domains
- [ ] ModSecurity::disable_domains
- [ ] ModSecurity::enable_all_domains
- [ ] ModSecurity::enable_domains
- [ ] ModSecurity::has_modsecurity_installed
- [ ] ModSecurity::list_domains
- [ ] Monitoring::create_contact
- [ ] Monitoring::create_site_monitor
- [ ] Monitoring::create_site_monitor_shopping_cart
- [ ] Monitoring::get_all_site_monitors
- [ ] Monitoring::get_build_cart_url
- [ ] Monitoring::get_completion_url
- [ ] Monitoring::get_contact
- [ ] Monitoring::get_site_monitor
- [ ] Monitoring::get_store_email_address
- [ ] Monitoring::get_user_status_from_store
- [ ] Monitoring::list_contacts
- [ ] Monitoring::load_user
- [ ] Monitoring::remove_contact
- [ ] Monitoring::remove_site_monitor
- [ ] Monitoring::remove_user
- [ ] Monitoring::save_user
- [ ] Monitoring::update_contact
- [x] Mysql::add_host
- [x] Mysql::add_host_note
- [x] Mysql::check_database
- [x] Mysql::create_database
- [x] Mysql::create_user
- [x] Mysql::delete_database
- [x] Mysql::delete_host
- [x] Mysql::delete_user
- [x] Mysql::dump_database_schema
- [x] Mysql::get_host_notes
- [x] Mysql::get_privileges_on_database
- [x] Mysql::get_restrictions
- [x] Mysql::get_server_information
- [x] Mysql::list_databases
- [x] Mysql::list_routines
- [x] Mysql::list_users
- [-] Mysql::locate_server
- [x] Mysql::rename_database
- [x] Mysql::rename_user
- [x] Mysql::repair_database
- [x] Mysql::revoke_access_to_database
- [x] Mysql::set_password
- [x] Mysql::set_privileges_on_database
- [-] Mysql::update_privileges
- [ ] NVData::get
- [ ] NVData::set
- [ ] NginxCaching::clear_cache
- [ ] NginxCaching::disable_cache
- [ ] NginxCaching::enable_cache
- [ ] NginxCaching::reset_cache_config
- [ ] Notifications::get_notifications_count
- [ ] Parser::firstfile_relative_uri
- [ ] PassengerApps::disable_application
- [ ] PassengerApps::edit_application
- [ ] PassengerApps::enable_application
- [ ] PassengerApps::ensure_deps
- [ ] PassengerApps::list_applications
- [ ] PassengerApps::register_application
- [ ] PassengerApps::unregister_application
- [ ] PasswdStrength::get_required_strength
- [ ] Personalization::get
- [ ] Personalization::set
- [ ] Plugins::can_show_promotions
- [ ] Plugins::get_uuid
- [ ] Plugins::reset_uuid
- [x] Postgresql::create_database
- [x] Postgresql::create_user
- [x] Postgresql::delete_database
- [x] Postgresql::delete_user
- [x] Postgresql::get_restrictions
- [x] Postgresql::grant_all_privileges
- [x] Postgresql::list_databases
- [x] Postgresql::list_users
- [x] Postgresql::rename_database
- [x] Postgresql::rename_user
- [-] Postgresql::rename_user_no_password
- [x] Postgresql::revoke_all_privileges
- [x] Postgresql::set_password
- [x] Postgresql::update_privileges
- [ ] Pushbullet::send_test_message
- [ ] Quota::get_local_quota_info
- [x] Quota::get_quota_info
- [x] Resellers::list_accounts
- [x] ResourceUsage::get_usages
- [-] Restore::directory_listing
- [-] Restore::get_users
- [-] Restore::query_file_info
- [-] Restore::restore_file
- [x] SSH::get_port
- [ ] SSL::add_autossl_excluded_domains
- [ ] SSL::can_ssl_redirect
- [ ] SSL::delete_cert
- [ ] SSL::delete_csr
- [ ] SSL::delete_key
- [ ] SSL::delete_ssl
- [ ] SSL::disable_mail_sni
- [ ] SSL::enable_mail_sni
- [ ] SSL::fetch_best_for_domain
- [ ] SSL::fetch_cert_info
- [ ] SSL::fetch_certificates_for_fqdns
- [ ] SSL::fetch_key_and_cabundle_for_certificate
- [ ] SSL::find_certificates_for_key
- [ ] SSL::find_csrs_for_key
- [ ] SSL::generate_cert
- [ ] SSL::generate_csr
- [ ] SSL::generate_key
- [ ] SSL::get_autossl_excluded_domains
- [ ] SSL::get_autossl_pending_queue
- [ ] SSL::get_autossl_problems
- [ ] SSL::get_cabundle
- [ ] SSL::get_cn_name
- [ ] SSL::install_ssl
- [ ] SSL::installed_host
- [ ] SSL::installed_hosts
- [ ] SSL::is_autossl_check_in_progress
- [ ] SSL::is_mail_sni_supported
- [ ] SSL::is_sni_supported
- [ ] SSL::list_certs
- [ ] SSL::list_csrs
- [ ] SSL::list_keys
- [ ] SSL::list_ssl_items
- [ ] SSL::mail_sni_status
- [ ] SSL::rebuild_mail_sni_config
- [ ] SSL::rebuildssldb
- [ ] SSL::remove_autossl_excluded_domains
- [ ] SSL::set_autossl_excluded_domains
- [ ] SSL::set_cert_friendly_name
- [ ] SSL::set_csr_friendly_name
- [ ] SSL::set_default_key_type
- [ ] SSL::set_key_friendly_name
- [ ] SSL::set_primary_ssl
- [ ] SSL::show_cert
- [ ] SSL::show_csr
- [ ] SSL::show_key
- [ ] SSL::start_autossl_check
- [ ] SSL::toggle_ssl_redirect_for_domains
- [ ] SSL::upload_cert
- [ ] SSL::upload_key
- [ ] ServerInformation::get_information
- [ ] ServiceProxy::get_service_proxy_backends
- [ ] ServiceProxy::set_service_proxy_backends
- [ ] ServiceProxy::unset_all_service_proxy_backends
- [ ] Session::create_temp_user
- [ ] Session::create_webmail_session_for_mail_user
- [ ] Session::create_webmail_session_for_mail_user_check_password
- [ ] Session::create_webmail_session_for_self
- [ ] SiteQuality::create_project
- [ ] SiteQuality::create_site_quality_user
- [ ] SiteQuality::delete_site_quality_user
- [ ] SiteQuality::get_all_scores
- [ ] SiteQuality::get_app_token
- [ ] SiteQuality::get_environment
- [ ] SiteQuality::has_site_quality_user
- [ ] SiteQuality::is_site_quality_user_enabled
- [ ] SiteQuality::reset_config
- [ ] SiteQuality::send_activation_email
- [ ] SiteQuality::verify_code
- [ ] SiteTemplates::list_site_templates
- [ ] SiteTemplates::list_user_settings
- [ ] SiteTemplates::publish
- [ ] Sitejet::add_api_token
- [ ] Sitejet::create_account
- [ ] Sitejet::create_restore_point
- [ ] Sitejet::create_website
- [ ] Sitejet::disk_quota_check
- [ ] Sitejet::do_not_delete_list
- [ ] Sitejet::get_all_sites_metadata
- [ ] Sitejet::get_all_user_sitejet_info
- [ ] Sitejet::get_api_token
- [ ] Sitejet::get_preview_url
- [ ] Sitejet::get_sitebuilder_domain_statuses
- [ ] Sitejet::get_sso_link
- [ ] Sitejet::get_templates
- [ ] Sitejet::get_user_site_metadata
- [ ] Sitejet::poll_publish
- [ ] Sitejet::publish
- [ ] Sitejet::restore_document_root
- [ ] Sitejet::set_template
- [ ] Sitejet::start_publish
- [x] SpamAssassin::clear_spam_box
- [x] SpamAssassin::get_symbolic_test_names
- [x] SpamAssassin::get_user_preferences
- [x] SpamAssassin::update_user_preference
- [x] Stats::get_bandwidth
- [x] Stats::get_site_errors
- [x] Stats::list_sites
- [-] Stats::list_stats_by_domain
- [x] StatsBar::get_stats
- [ ] StatsManager::get_configuration
- [ ] StatsManager::save_configuration
- [ ] SubDomain::addsubdomain
- [ ] Team::add_roles
- [ ] Team::add_team_user
- [ ] Team::edit_team_user
- [ ] Team::list_team
- [ ] Team::list_team_ui
- [ ] Team::remove_roles
- [ ] Team::remove_team_user
- [ ] Team::set_contact_email
- [ ] Team::set_notes
- [ ] Team::set_password
- [ ] Team::set_roles
- [ ] Team::suspend_team_user
- [ ] Team::unsuspend_team_user
- [ ] TeamRoles::list_feature_descriptions
- [x] Themes::get_theme_base
- [x] Themes::list
- [x] Themes::update
- [ ] Tokens::create_full_access
- [ ] Tokens::list
- [ ] Tokens::rename
- [ ] Tokens::revoke
- [ ] TwoFactorAuth::generate_user_configuration
- [ ] TwoFactorAuth::get_team_user_configuration
- [ ] TwoFactorAuth::get_user_configuration
- [ ] TwoFactorAuth::remove_user_configuration
- [ ] TwoFactorAuth::set_user_configuration
- [x] UserManager::check_account_conflicts
- [ ] UserManager::create_user
- [ ] UserManager::delete_user
- [ ] UserManager::dismiss_merge
- [ ] UserManager::edit_user
- [x] UserManager::list_users
- [x] UserManager::lookup_service_account
- [x] UserManager::lookup_user
- [ ] UserManager::merge_service_account
- [ ] UserManager::unlink_service_account
- [ ] UserTasks::delete
- [ ] UserTasks::retrieve
- [ ] Variables::get_server_information
- [ ] Variables::get_session_information
- [x] Variables::get_user_information
- [ ] VersionControl::create
- [ ] VersionControl::delete
- [ ] VersionControl::retrieve
- [ ] VersionControl::update
- [ ] VersionControlDeployment::create
- [ ] VersionControlDeployment::delete
- [ ] VersionControlDeployment::retrieve
- [ ] WebDisk::delete_user
- [ ] WebDisk::set_homedir
- [ ] WebDisk::set_password
- [ ] WebDisk::set_permissions
- [ ] WebVhosts::list_domains
- [ ] WebVhosts::list_ssl_capable_domains
- [x] WebmailApps::list_webmail_apps
- [ ] WordPressSite::create
- [ ] WordPressSite::retrieve
- [x] cPAddons::get_available_addons
- [x] cPAddons::get_instance_settings
- [x] cPAddons::list_addon_instances
- [ ] cPGreyList::disable_all_domains
- [ ] cPGreyList::disable_domains
- [ ] cPGreyList::enable_all_domains
- [ ] cPGreyList::enable_domains
- [ ] cPGreyList::has_greylisting_enabled
- [ ] cPGreyList::list_domains
