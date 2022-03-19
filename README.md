# FYP-VPN
### VPN Management system for the Final Year Project

- VPN Server & Client side management website
- MFA authentication for admin
- SSO(Google login) for user

### 1. System update & dependency

##### On shell ($)
```bash
sudo dnf update -y && sudo dnf install -y curl wget make unzip vim gcc gcc-c++ git git-lfs python3-pip && git lfs install
```

### 1-2. Install wireguard client

##### On shell ($)
```bash
cd ~ && git clone https://github.com/sshyunleee0000/FYP-VPN.git
cd FYP-VPN/central_server && python3 client-install.py
```
##### After get allowed
```bash
sudo wg-quick up wg0 && sudo wg
```

##### Stop using
```bash
sudo wg-quick down wg0
```

### 2. Install wireguard server

##### On shell ($)
```bash
cd ~ && git clone https://github.com/sshyunleee0000/FYP-VPN.git
cd FYP-VPN/central_server && python3 install.py
```
- Save the Server Key and Server IP

### 3. Setting Website

##### On shell ($)
Path = FYP-VPN/central_server
```bash
python3 web-setting.py
```

### 4. Setting OTP
Admin site: http://localhost:8000/admin/
##### On Admin 'Add TOTP devices' Page
- Add TOTP device

##### On shell ($)
Path = FYP-VPN/central_server
```bash
python3 set-otp.py
```
