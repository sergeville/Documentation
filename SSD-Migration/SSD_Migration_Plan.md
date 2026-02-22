# SanDisk PRO-G40 SSD Migration Plan

> **✅ MIGRATION COMPLETE** - This plan was successfully executed on 2026-01-21.
> All major tasks completed. See MIGRATION_COMPLETE_SUMMARY.md for full results.
>
> **⚠️ DO NOT RE-RUN THIS MIGRATION**
> This migration has already been completed. Re-running these steps could cause:
> - Data loss or duplication
> - Broken symlinks
> - System instability
>
> If you need to verify the current state, use:
> - `check-migration` - Check migration status
> - `verify-docker` - Verify Docker SSD configuration
> - `check-backup` - Check backup drive status

**Goal**: Move files from Mac internal HD to external SSD to free up space while maintaining system stability

**Date Created**: 2026-01-19
**Date Completed**: 2026-01-21 3:20 PM
**Last Updated**: 2026-01-22 (Added completion status and home reorganization)
**Status**: ✅ Complete - 252GB freed, Ollama and venv symlinked, Docker copied to SSD

---

## Safety Principles

1. **COPY FIRST, DELETE LATER** - Never delete original files until you've verified the copies work
2. **ALWAYS HAVE A BACKUP** - Complete Time Machine backup before starting
3. **USE SYMLINKS** - Applications will still find files in expected locations
4. **AUTO-MOUNT REQUIRED** - External SSD must mount automatically on startup
5. **TEST BEFORE REMOVING** - Verify everything works before deleting originals

---

## What Files to Move vs Keep

### SAFE TO MOVE (Large Space Savers)
- Documents/
- Downloads/
- Movies/
- Music/
- Pictures/
- Desktop/ (optional)
- Large project folders
- Virtual machine images (.vmdk, .vdi, .qcow2)
- Docker images/containers
- **~/.ollama/ (AI models - Ollama LLMs)**
- Old archives and backups
- Video/audio projects

### KEEP ON INTERNAL DRIVE (Critical for System)
- Applications/
- Library/ (most of it)
- .ssh/
- .config/
- .zshrc, .bashrc, .bash_profile
- Any dotfiles (hidden files starting with .)
- System preferences and settings
- Active development dependencies (node_modules, venv, etc.)

### SELECTIVE (Evaluate Size First)
- Code/ or Development/ folders
- Creative software caches (can be large but may slow down if external)
- Browser profiles (can be large)

---

## Step-by-Step Migration Process

### Phase 1: Preparation

#### Task 1: Verify SSD Connection
```bash
diskutil list
```
- Look for your SanDisk PRO-G40 in the output
- Note the disk identifier (e.g., disk2, disk3)

#### Task 2: Format the SSD
- Open **Disk Utility** (Applications > Utilities > Disk Utility)
- Select the SanDisk PRO-G40 (select the drive, not a partition)
- Click **Erase**
- Settings:
  - Name: `ProG40` (no spaces recommended)
  - Format: `APFS`
  - Scheme: `GUID Partition Map`
- Click **Erase** and wait for completion

#### Task 3: Create Time Machine Backup
- Ensure your existing Time Machine backup is current
- Go to System Settings > General > Time Machine
- Click "Back Up Now"
- Wait for backup to complete (DO NOT SKIP THIS)

#### Task 4: Check Space Usage
```bash
# Check what's using space in your home directory
du -sh ~/Documents ~/Downloads ~/Movies ~/Music ~/Pictures ~/Desktop
du -sh ~/*
```
- Identify the largest folders
- Verify external SSD has enough space

---

### Phase 2: Create Structure and Copy Files

#### Task 5: Create Directory Structure on SSD
```bash
# Create main folder on external SSD
mkdir -p /Volumes/ProG40/HomeFiles

# Create subdirectories matching your home layout
mkdir -p /Volumes/ProG40/HomeFiles/Documents
mkdir -p /Volumes/ProG40/HomeFiles/Downloads
mkdir -p /Volumes/ProG40/HomeFiles/Movies
mkdir -p /Volumes/ProG40/HomeFiles/Music
mkdir -p /Volumes/ProG40/HomeFiles/Pictures
mkdir -p /Volumes/ProG40/HomeFiles/.ollama
mkdir -p /Volumes/ProG40/HomeFiles/Docker
mkdir -p /Volumes/ProG40/HomeFiles/venv
# Add other folders as needed
```

#### Task 6: Copy Files to External SSD
Start with one folder to test the process:

```bash
# Example: Copy Documents first
rsync -av --progress ~/Documents/ /Volumes/ProG40/HomeFiles/Documents/
```

**Important rsync flags**:
- `-a`: Archive mode (preserves permissions, timestamps, symlinks)
- `-v`: Verbose output
- `--progress`: Show progress during transfer

Repeat for each folder you want to move:
```bash
rsync -av --progress ~/Downloads/ /Volumes/ProG40/HomeFiles/Downloads/
rsync -av --progress ~/Movies/ /Volumes/ProG40/HomeFiles/Movies/
rsync -av --progress ~/Music/ /Volumes/ProG40/HomeFiles/Music/
rsync -av --progress ~/Pictures/ /Volumes/ProG40/HomeFiles/Pictures/

# Copy Ollama AI models (11GB - large LLM files)
rsync -av --progress ~/.ollama/ /Volumes/ProG40/HomeFiles/.ollama/

# Copy Docker and venv if needed
rsync -av --progress ~/Library/Containers/com.docker.docker/Data/ /Volumes/ProG40/HomeFiles/Docker/
```

#### Task 7: Verify Copied Files
```bash
# Compare file counts
ls -R ~/Documents | wc -l
ls -R /Volumes/ProG40/HomeFiles/Documents | wc -l

# Check sizes match
du -sh ~/Documents
du -sh /Volumes/ProG40/HomeFiles/Documents

# Verify a few files manually
# Open some files from the external SSD to ensure they work
```

---

### Phase 3: Create Symlinks (THE CRITICAL PART)

#### Task 8: Rename Original and Create Symlinks

**For each folder you've copied and verified:**

```bash
# Example for Documents folder:

# 1. Rename the original (keeps it as backup)
mv ~/Documents ~/Documents.backup

# 2. Create symbolic link
ln -s /Volumes/ProG40/HomeFiles/Documents ~/Documents

# 3. Verify the link works
ls -la ~ | grep Documents
# Should show: Documents -> /Volumes/ProG40/HomeFiles/Documents

# 4. Test by opening a file
open ~/Documents
```

Repeat for each folder:
```bash
mv ~/Downloads ~/Downloads.backup
ln -s /Volumes/ProG40/HomeFiles/Downloads ~/Downloads

mv ~/Movies ~/Movies.backup
ln -s /Volumes/ProG40/HomeFiles/Movies ~/Movies

mv ~/Music ~/Music.backup
ln -s /Volumes/ProG40/HomeFiles/Music ~/Music

mv ~/Pictures ~/Pictures.backup
ln -s /Volumes/ProG40/HomeFiles/Pictures ~/Pictures

# Ollama models (hidden folder)
mv ~/.ollama ~/.ollama.backup
ln -s /Volumes/PRO-G40/HomeFiles/.ollama ~/.ollama

# Docker and venv if applicable
mv ~/venv ~/venv.backup
ln -s /Volumes/PRO-G40/HomeFiles/venv ~/venv
```

---

### Phase 4: Testing and Configuration

#### Task 9: Test Applications
- Open Finder and navigate to each symlinked folder
- Open files from each folder to verify apps can access them
- Try saving new files to these locations
- Test any critical applications (Photos app, Music app, etc.)
- Leave everything running for a day or two to ensure stability

#### Task 10: Configure Auto-Mount on Login
```bash
# Get the UUID of the external drive
diskutil info /Volumes/ProG40 | grep UUID

# Add to /etc/fstab (alternative method: use Disk Utility)
# Or use System Settings:
```
- System Settings > General > Login Items
- Click the `+` under "Open at Login"
- Navigate to `/Volumes/ProG40` and add it

**Alternative: Create a launch agent** (more reliable)
- If needed, we can create a custom launch agent for auto-mounting

#### Task 11: Update Time Machine
- System Settings > General > Time Machine
- Options > Exclude items
- Verify that `/Volumes/ProG40/HomeFiles` is included in backups
- Add the `.backup` folders to exclusions temporarily

---

### Phase 5: Cleanup

#### Task 12: Remove Backup Folders (After 1-2 weeks of testing)
**ONLY after confirming everything works perfectly:**

```bash
# Check space used by backup folders
du -sh ~/Documents.backup ~/Downloads.backup ~/Movies.backup ~/Music.backup ~/Pictures.backup

# Remove them ONE AT A TIME after verification
rm -rf ~/Documents.backup
# Wait and verify Documents still works from symlink

rm -rf ~/Downloads.backup
# Verify Downloads works

# Continue for each folder...
```

#### Task 13: Monitor and Maintain
- Check that external SSD auto-mounts after restart
- Verify symlinks remain intact
- Monitor Time Machine backups include external files
- Keep at least 20-30GB free on internal drive

---

## Emergency Recovery Procedures

### If External SSD Fails to Mount
```bash
# Temporary fix: mount manually
diskutil mount ProG40

# Check why it didn't auto-mount
diskutil info /Volumes/ProG40
```

### If You Need to Restore Original Files
```bash
# If you still have .backup folders:
rm ~/Documents  # Remove symlink
mv ~/Documents.backup ~/Documents  # Restore original

# If backups are deleted, restore from Time Machine
# Enter Time Machine and navigate to home directory
# Select the date before migration
# Restore needed folders
```

### If Symlinks Break
```bash
# Check if link is broken
ls -la ~/Documents

# Recreate symlink
rm ~/Documents
ln -s /Volumes/ProG40/HomeFiles/Documents ~/Documents
```

---

## Expected Space Savings

To estimate space savings:
```bash
# Run before migration
df -h /
du -sh ~/*

# Run after migration and cleanup
df -h /
```

Typical savings depend on what you move:
- Documents: 5-50GB (Your system: 4.4GB)
- Downloads: 10-100GB
- Movies: 50-500GB+
- Music: 10-100GB
- Pictures: 20-200GB (Your system: 2GB)
- **Ollama AI models: 5-50GB (Your system: 11GB with llama3, llama3.1-8b, llama3.2)**
- **Docker data: 50-500GB (Your system: 240GB)**
- **venv/virtual environments: 1-10GB (Your system: 1GB)**

**Your migration total: ~258GB freed from internal drive**

---

## Important Warnings

1. **Never eject the external SSD while your Mac is running** - Apps will fail
2. **Don't rename the SSD** - Symlinks will break
3. **Don't move the mount point** - Keep it at `/Volumes/ProG40`
4. **Keep the SSD connected** - If you need to disconnect, restore originals first
5. **USB/Thunderbolt cable quality matters** - Use the cable that came with the drive

---

## Troubleshooting

### Problem: External drive won't mount on startup
**Solution**: Check System Settings > Login Items, or create a launch agent

### Problem: App says it can't find files
**Solution**: Check if drive is mounted, verify symlink is intact

### Problem: Slow performance
**Solution**: Ensure SSD is connected via fast port (Thunderbolt/USB-C 3.1+), not USB 2.0

### Problem: "File in use" errors during copy
**Solution**: Close all applications, try again, or skip and handle individually

---

## Commands Reference

```bash
# Check disk space
df -h

# Check folder sizes
du -sh ~/folder_name

# List all volumes
ls -la /Volumes/

# Check mount status
mount | grep ProG40

# Verify symlinks
ls -la ~ | grep ^l

# Force mount drive
diskutil mount ProG40

# Safely eject (only when not in use!)
diskutil eject ProG40
```

---

## Notes

- This document should be kept on your internal drive
- Review this plan before starting each phase
- Don't rush - the .backup folders protect you during testing
- When in doubt, ask before deleting anything

---

**Current Status**: Plan created, ready to begin Phase 1
