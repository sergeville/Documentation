# Post-Restart Verification Test

> **✅ ALL TESTS PASSED SUCCESSFULLY**
> These verification tests were completed successfully after migration.
> System is stable and all services are working correctly.

## Test after restart - Verify everything still works after rebooting

### Pre-Restart Checklist
- [ ] PRO-G40 SSD is connected
- [ ] All applications are closed
- [ ] No active file transfers

### After Restart - Verification Steps

#### 1. SSD Auto-Mount
```bash
# Verify SSD mounted automatically
ls /Volumes/PRO-G40
```
**Expected**: Folder should exist and be accessible

---

#### 2. Docker Desktop
```bash
# Wait for Docker to start, then check containers
docker ps
```
**Expected**: All 4 containers running (Home Assistant, Alfred Agent, Mosquitto, Ollama)

---

#### 3. Ollama Models
```bash
# List Ollama models
ollama list
```
**Expected**: Shows llama3.1:8b, llama3.2:latest, llama3.2:3b

---

#### 4. LM Studio
```bash
# Check LM Studio models accessible
ls ~/.lmstudio/models/mlx-community/
find ~/.lmstudio/models -name "*.safetensors" | wc -l
```
**Expected**: gpt-oss-20b-MXFP4-Q8 folder exists, 3 safetensors files found

---

#### 5. Python venv
```bash
# Verify venv symlink works
ls ~/venv/
```
**Expected**: venv folder contents visible

---

#### 6. Apple Wallpapers
```bash
# Check wallpaper videos accessible
ls ~/Library/Application\ Support/com.apple.wallpaper/aerials/videos/ | wc -l
```
**Expected**: Shows 20 videos

---

#### 7. Verify All Symlinks
```bash
# List all symlinks
ls -la ~ | grep "^l" | grep -E "(ollama|venv|lmstudio)"
ls -la ~/Library/Application\ Support/ | grep wallpaper
```
**Expected**:
- `.lmstudio -> /Volumes/PRO-G40/HomeFiles/.lmstudio`
- `.ollama -> /Volumes/PRO-G40/HomeFiles/.ollama`
- `venv -> /Volumes/PRO-G40/HomeFiles/venv`
- `com.apple.wallpaper -> /Volumes/PRO-G40/HomeFiles/apple-wallpaper`

---

#### 8. Disk Space Check
```bash
# Verify space savings maintained
df -h / /Volumes/PRO-G40
```
**Expected**:
- Internal HD: ~11GB used, ~93GB free
- PRO-G40: ~101GB used, ~830GB free

---

### If Any Test Fails

#### SSD Not Mounted
```bash
# Mount manually
diskutil mount PRO-G40

# Check auto-mount agent
launchctl list | grep mount-prog40
```

#### Broken Symlink
```bash
# For any broken symlink, recreate it:
# Example for .ollama:
rm ~/.ollama
ln -s /Volumes/PRO-G40/HomeFiles/.ollama ~/.ollama
```

#### Docker Not Working
```bash
# Check if Docker.raw symlink is intact
ls -la ~/Library/Containers/com.docker.docker/Data/vms/0/data/Docker.raw

# Restart Docker Desktop
osascript -e 'quit app "Docker"'
sleep 5
open -a Docker
```

---

### All Tests Pass? ✅

If all tests pass after restart:
- ✅ Migration is successful and stable
- ✅ System is ready for daily use
- ✅ PRO-G40 SSD is properly integrated
- ✅ Auto-mount is working correctly

---

**Migration Date**: January 21, 2026
**Total Space Migrated**: ~78GB
**Active Symlinks**: 5
