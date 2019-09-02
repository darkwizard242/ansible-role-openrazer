Ansible Role: openrazer
=========

Role to install (_by default_) `openrazer-meta` package  or uninstall (_if  passed as var_)  on **Ubuntu** systems.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below (located in  `defaults/main.yml`):

```yaml
openrazer_repo: 'ppa:openrazer/stable'
openrazer_repo_desired_state: present
openrazer_repo_filename: openrazer
openrazer_app: openrazer-meta
openrazer_package_desired_state: present
```

Variable `openrazer_repo`: Refers to the ppa repo to add.

Variable `openrazer_repo_desired_state`: Defined to dynamically chose whether to add/keep (i.e. `present`) or remove (i.e. `absent`) the repository file list from `/etc/apt/sources.list.d`.

Variable `openrazer_repo_filename`: Defined to set th repository file name for saving in `/etc/apt/sources.list.d`

Variable `openrazer_app`: Defines the app to install i.e. **openrazer-meta**

Variable `openrazer_package_desired_state`: Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package.

Dependencies
------------

None

Example Playbook
----------------

For default behaviour of role (i.e. installation of **openrazer** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.openrazer
```

For customizing behavior of role (i.e. installation of latest **openrazer** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.openrazer
      vars:
        openrazer_package_desired_state: latest
```
             
For customizing behavior of role (i.e. un-installation of **openrazer** package) in ansible playbooks.
```yaml
- hosts: servers
  roles:
    - role: darkwizard242.openrazer
      vars:
        openrazer_package_desired_state: absent
```      
         
License
-------

[MIT](https://github.com/darkwizard242/ansible-role-openrazer/blob/master/LICENSE)

Author Information
------------------

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
