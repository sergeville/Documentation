# SSD Migration Master Guide

> **✅ ALL TASKS COMPLETED SUCCESSFULLY** - Migration finished 2026-01-21.
> This guide was used to successfully migrate 252GB to PRO-G40 SSD.
> See MIGRATION_COMPLETE_SUMMARY.md for detailed results.
>
> **⚠️ DO NOT RE-EXECUTE THESE PROCEDURES**
> The migration is complete. Re-running migration commands could cause:
> - Overwriting existing data
> - Breaking working symlinks
> - System instability
>
> This document is kept for **reference only**.

**Drive:** SanDisk PRO-G40
**Mount Point:** /Volumes/PRO-G40
**Status:** ✅ Complete - All procedures successfully executed

This comprehensive guide combines the migration strategy with safety scripts, troubleshooting steps, and automation to keep your system stable.

---

## 1. Safety Principles & Prep

* **Copy First, Delete Later**: Never delete original files until you've verified the copies work.
* **Always Have a Backup**: Complete a Time Machine backup before starting.
* **Use Symlinks**: Applications will still find files in expected locations via pointers.
* **Full Disk Access**: Grant Terminal "Full Disk Access" in System Settings to allow tmutil commands if you need to pause backups during the move.

---

## 2. Active Transfer Monitoring

Run this in a new Terminal tab to alert you when your file transfer completes:

```bash
while pgrep -x "rsync" > /dev/null; do sleep 60; done; osascript -e 'display notification "Rsync Migration Complete!" with title "SSD Migration"'; say "Migration complete"
```

---

## 3. Post-Transfer Verification

Before creating symlinks, run these checks:

* **Size Check**:
  ```bash
  du -sh ~/Documents /Volumes/PRO-G40/HomeFiles/Documents
  ```

* **File Count**:
  ```bash
  echo "SSD Documents Count:" && find /Volumes/PRO-G40/HomeFiles/Documents -type f | wc -l
  ```

* **Integrity Sampling**: Manually open a high-priority file from the SSD destination.

---

## 4. Symlink Deployment

Run these only after verification is 100% successful:

```bash
# Documents
mv ~/Documents ~/Documents.backup && ln -s /Volumes/PRO-G40/HomeFiles/Documents ~/Documents

# Pictures
mv ~/Pictures ~/Pictures.backup && ln -s /Volumes/PRO-G40/HomeFiles/Pictures ~/Pictures

# Ollama Models
mv ~/.ollama ~/.ollama.backup && ln -s /Volumes/PRO-G40/HomeFiles/.ollama ~/.ollama
```

---

## 5. System Health & Automation

### A. The Shell "Mount Guard"

Add this to your `~/.zshrc` to prevent apps from launching if the drive is missing:

```bash
check_ssd() {
    if [ ! -d "/Volumes/PRO-G40" ]; then
        echo "❌ CRITICAL ERROR: PRO-G40 SSD is not mounted."
        return 1
    fi
}
alias docker='check_ssd && docker'
alias ollama='check_ssd && ollama'
alias code='check_ssd && code'
```

After adding this, reload your shell:
```bash
source ~/.zshrc
```

### B. Wake-from-Sleep Health Check

**Step 1:** Create the health check script at `~/check_ssd_health.sh`:

```bash
#!/bin/bash
MOUNT_PATH="/Volumes/PRO-G40"
if [ ! -d "$MOUNT_PATH" ]; then
    osascript -e 'display alert "SSD Connection Error" message "PRO-G40 drive is missing!"'
fi
```

**Step 2:** Make it executable:
```bash
chmod +x ~/check_ssd_health.sh
```

**Step 3:** Create the Launch Agent at `~/Library/LaunchAgents/com.user.ssdcheck.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.ssdcheck</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>~/check_ssd_health.sh</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StartInterval</key>
    <integer>300</integer>
</dict>
</plist>
```

**Step 4:** Load the Launch Agent:
```bash
launchctl load ~/Library/LaunchAgents/com.user.ssdcheck.plist
```

This will check your SSD every 5 minutes (300 seconds) and alert you if it's disconnected.

---

## 6. Troubleshooting & Emergencies

* **Drive Not Connected**: Do not launch Docker or Ollama until the drive is visible in Finder.
* **Broken Symlinks**: If the link turns red, unplug the SSD, delete any "dummy" empty folders in /Volumes/PRO-G40, and reconnect.
* **Emergency Revert**:
  ```bash
  # If the SSD fails, revert to your backup:
  rm ~/Documents
  mv ~/Documents.backup ~/Documents
  ```
* **Disable Launch Agent**:
  ```bash
  launchctl unload ~/Library/LaunchAgents/com.user.ssdcheck.plist
  ```

---

## Quick Reference Commands

**Check if SSD is mounted:**
```bash
ls -la /Volumes/PRO-G40
```

**Verify symlinks:**
```bash
ls -la ~ | grep -E 'Documents|Pictures|.ollama'
```

**Monitor disk usage:**
```bash
df -h /Volumes/PRO-G40
```