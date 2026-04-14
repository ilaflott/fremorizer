# Phase 3 Feature Issues - Quick Start Guide

This guide helps you create individual GitHub issues for each Phase 3 deferred feature.

## Overview

8 individual issues need to be created, one for each of the following features:

1. PR #832: Harden branded-variable disambiguations
2. PR #833: Improved omission tracking
3. PR #834: New `fremor init` command for config fetching
4. PR #836: Informative error on mip_era/table format mismatch
5. PR #837: Accept CF calendar aliases (noleap/365_day, etc.)
6. PR #838: CMIP7 flavored tests
7. PR #846: Variable list semantics (map modeler vars to MIP table names)
8. PR #817: Update cmor to 3.14.2

## Recommended Approach

### Option A: Automated Creation (Fastest)

If you have GitHub authentication set up:

```bash
# Using the shell script
cd /home/runner/work/fremorizer/fremorizer/.github
./create_phase3_issues.sh

# OR using the Python script (requires PyGithub)
pip install PyGithub
export GITHUB_TOKEN="your_token_here"
python create_phase3_issues.py --create
```

### Option B: Manual Creation via GitHub Web UI

1. Open the file `.github/PHASE_3_ISSUES.md` in this repository
2. For each issue section (there are 8 total):
   - Go to https://github.com/ilaflott/fremorizer/issues/new
   - Copy the **title** from the issue section
   - Copy the **body** content from the issue section
   - Add the **labels** listed in the issue section
   - Click "Submit new issue"
3. Record the issue numbers created

### Option C: Using GitHub CLI manually

For each issue in `.github/PHASE_3_ISSUES.md`:

```bash
gh issue create \
  --repo ilaflott/fremorizer \
  --title "COPY_TITLE_HERE" \
  --body "COPY_BODY_HERE" \
  --label "COPY_LABELS_HERE"
```

## After Creating Issues

Once all 8 issues are created:

1. **Update tracking issue #27** with links to all new issues
2. **Optionally create a GitHub Project board** to track Phase 3 implementation
3. **Consider adding milestone** "Phase 3" to group these issues
4. **Verify labels** are applied correctly to all issues

## Troubleshooting

**Problem**: `gh` CLI returns 403 Forbidden
- **Solution**: Ensure you have proper GitHub authentication configured
- Run `gh auth status` to check
- Run `gh auth login` if needed

**Problem**: PyGithub not installed
- **Solution**: `pip install PyGithub`

**Problem**: Missing labels in repository
- **Solution**: The following labels should exist in the repository:
  - `enhancement`
  - `phase-3` (create if needed)
  - `new-feature` (create if needed)
  - `error-handling` (create if needed)
  - `compatibility` (create if needed)
  - `testing`
  - `cmip7` (create if needed)
  - `high-priority` (create if needed)
  - `variable-mapping` (create if needed)
  - `dependencies` (create if needed)

## Files in This Directory

- `PHASE_3_ISSUES.md` - Complete issue templates (the source of truth)
- `README_PHASE_3_ISSUES.md` - Detailed documentation
- `create_phase3_issues.sh` - Bash script for automated creation
- `create_phase3_issues.py` - Python script for automated creation
- `QUICKSTART_PHASE_3_ISSUES.md` - This file

## Next Steps After Issues Are Created

1. Review Phase 2.5 equivalence testing status
2. Prioritize which Phase 3 features to implement first
3. Begin implementation of highest priority items
4. Update PHASE_3_DEFERRED_FEATURES.md with issue links
