# Individual Project (60%)-Theme 2 — Networking: Virtualised Lab (Windows 10 + Xubuntu)

Oracle VirtualBox lab with dual-adapter networking (NAT + Host-Only), connectivity testing (ICMP/DNS/Traceroute), and SQLite CRUD logging using DB Browser.

Contents

Architecture

Prerequisites

VM Setup

Network Configuration

OS Configuration (Least Privilege)

Connectivity Tests

SQLite Logging (CRUD)

Troubleshooting

Screenshots (placeholders)

Architecture

Two VMs on VirtualBox:

Windows 10

Adapter 1: NAT (internet access)

Adapter 2: Host-Only (192.168.56.0/24)

Xubuntu

Adapter 1: Host-Only only (192.168.56.0/24)

Target addressing used during tests:

Windows (Host-Only): 192.168.56.101
Xubuntu (Host-Only): 192.168.56.102

Prerequisites

Oracle VirtualBox (latest)

Windows 10 ISO, Xubuntu ISO

DB Browser for SQLite (Windows) and/or sqlite3 CLI

Basic shell tools (PowerShell on Win, Terminal on Xubuntu)

VM Setup

Minimal recommended resources:

Windows: CPU ≥ 2, RAM 4 GB, Disk 25+ GB

Xubuntu: CPU ≥ 2, RAM 2 GB, Disk 20 GB

Create VMs, attach ISOs, install OSs, then add the network adapters as per Architecture.

Network Configuration
VirtualBox (per VM)

Adapter 1 (Windows): Attached to: NAT

Adapter 2 (Windows & Xubuntu): Attached to: Host-only Adapter
Host-only network: 192.168.56.0/24

Verify addressing

Windows (PowerShell):

ipconfig
## Note IPv4 Host-Only: 192.168.56.101
## Note NAT IPv4: 10.0.2.15 (typical)


Xubuntu (Terminal):

ip a
## Look for enp0s3 on 192.168.56.0/24, e.g., 192.168.56.102

OS Configuration (Least Privilege)

Create separate Administrator and Standard users.

Windows (PowerShell as Admin):

## Create standard user (example)
net user student P@ssw0rd! /add
net localgroup "Users" student /add

## (Optional) add/remove from Administrators
## net localgroup "Administrators" student /add


Xubuntu:

## Create a standard user and set password
sudo adduser student
## Grant sudo only if required for setup
sudo usermod -aG sudo student


Operate day-to-day tests as standard user; elevate only when necessary (Run as administrator / sudo).

Connectivity Tests
1) VM ↔ VM ICMP

Windows → Xubuntu:

ping 192.168.56.102


Xubuntu → Windows:

ping -c 4 192.168.56.101

2) DNS resolution

Windows (via NAT):

nslookup www.google.com


Xubuntu (Host-Only, expect failure if no NAT):

dig www.google.com
## or
nslookup www.google.com

3) Traceroute

Windows:

tracert 8.8.8.8


Xubuntu:

traceroute 8.8.8.8


Expected behaviour:

Windows resolves DNS and shows multi-hop traceroute via NAT.

Xubuntu shows only local gateway hop and DNS fails (isolated Host-Only).

SQLite Logging (CRUD)
Option A — DB Browser for SQLite (GUI)

Create a database (e.g., networking.db) and a table network_logs:

Schema

CREATE TABLE IF NOT EXISTS network_logs (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    Name       TEXT    NOT NULL, -- Source system
    Target     TEXT    NOT NULL, -- Destination/IP/Domain
    Timestamp  INTEGER NOT NULL, -- Unix epoch (or TEXT datetime)
    TestType   TEXT    NOT NULL, -- Ping | DNS | Traceroute
    Result     TEXT    NOT NULL  -- Success | Fail | Blocked | Notes
);


C – Create (INSERT)

INSERT INTO network_logs (Name, Target, Timestamp, TestType, Result)
VALUES ('Windows', '192.168.56.102', strftime('%s','now'), 'Ping', 'Success');

INSERT INTO network_logs (Name, Target, Timestamp, TestType, Result)
VALUES ('Windows', 'www.google.com', strftime('%s','now'), 'DNS', 'Success');

INSERT INTO network_logs (Name, Target, Timestamp, TestType, Result)
VALUES ('Xubuntu', 'www.google.com', strftime('%s','now'), 'DNS', 'Blocked (Host-Only)');


R – Read (SELECT)

SELECT id, Name, Target, datetime(Timestamp,'unixepoch') AS ts, TestType, Result
FROM network_logs
ORDER BY id DESC;


U – Update

UPDATE network_logs
SET Result = 'Success (latency < 5ms)'
WHERE id = 1;


D – Delete

DELETE FROM network_logs
WHERE id = 3; -- example

Option B — CLI (sqlite3)
sqlite3 networking.db <<'SQL'
.read schema.sql
INSERT INTO network_logs (Name, Target, Timestamp, TestType, Result)
VALUES ('Xubuntu','192.168.56.101', strftime('%s','now'), 'Ping', 'Success');
SELECT * FROM network_logs;
SQL

Minimal CRUD pseudocode (language-agnostic)
CONNECT to networking.db

CREATE TABLE network_logs (...schema above...)

function insertLog(Name, Target, Timestamp, TestType, Result):
    INSERT INTO network_logs (Name, Target, Timestamp, TestType, Result)
    VALUES (Name, Target, Timestamp, TestType, Result)

function readLogs():
    SELECT * FROM network_logs ORDER BY id DESC

function updateLog(id, newResult):
    UPDATE network_logs SET Result = newResult WHERE id = id

function deleteLog(id):
    DELETE FROM network_logs WHERE id = id

Troubleshooting
Linux apt “temporary failure resolving” / “read-only file system”

If you see errors like:

Temporary failure resolving 'gb.archive.ubuntu.com'
E: Could not create temporary file ... Read-only file system


Check:

Networking mode — if the VM has only Host-Only, it won’t reach the internet.

Add a NAT adapter (or temporarily switch Adapter 1 to NAT) to pull packages.

Disk/ISO state — ensure the virtual disk is not mounted read-only (Power outage / improper shutdown can trigger FS checks).

Remount root RW then update:

sudo mount -o remount,rw /
sudo apt update && sudo apt -y upgrade

Screenshots (placeholders)

Add the images you captured in your report into a figures/ folder and reference them here (and/or in your doc):

figures/win-ipconfig.png — Windows ipconfig

figures/xubu-ip-a.png — Xubuntu ip a

figures/win-ping-xubuntu.png — Ping Win→Xubuntu

figures/xubu-ping-win.png — Ping Xubuntu→Win

figures/win-nslookup.png — Windows nslookup

figures/xubu-dig-fail.png — Xubuntu dig

figures/win-tracert-8-8-8-8.png — tracert

figures/sqlite-table.png — DB schema

figures/sqlite-crud.png — CRUD in DB Browser

Example Markdown embed:

![Windows ipconfig](figures/win-ipconfig.png)

### License / Academic Integrity

All tests were executed on private VMs under VirtualBox (Host-Only/NAT). No scanning of external systems was performed. Logs and screenshots are my own work.