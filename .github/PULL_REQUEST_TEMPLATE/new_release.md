To publish new release, cease merging new PRs to `main`, and carefully follow the below procedure:


### first, create a new tag for release

- [ ] create a new branch off of `main`, which should be the previous tagged version + `.post`, *give it a name different than the exact tag you are creating*
- [ ] edit the version number in `fremor/_version.py` from the current one, to the desired version tag, remove `.post`, then open a PR to `main` in this repository.
- [ ] confirm the branch is functional by letting workflows finish, if you see green checks only, proceed. otherwise, stop and debug.
- [ ] at this point, light clean up style edits are OK, but functional edits are not. Do so until happy and keep the checks passing.
- [ ] now create the tag from the branch at this point locally in your terminal with `git tag X.Y.Z;`


### second, publish release to PyPI, then github, in that order

- [ ] now push your tag you created locally with `git checkout X.Y.Z; git push origin HEAD:refs/tags/X.Y.Z`
- [ ] workflow checks are triggered by the new push to the new tag `X.Y.Z`, and one of the workflows will to publish the built package to `PyPI`, check the actions tab

WARNING: *any problems or mistakes after the next step are irreversible due to package immutability so make sure things are working before continuing*

- [ ] on github, create a new release from the new tag, generate release notes automatically comparing to the previous tag, and upload the built `X.Y.Z` package downloaded from `PyPI` *you cannot do this later due to immutability of releases*


### third, publish release to `conda-forge` via `fremor-feedstock` fork

- [ ] use (create if needed) a fork (e.g. https://github.com/ilaflott/fremor-feedstock) to create a new branch called `fremorX.Y.Z`, e.g. https://github.com/ilaflott/fremor-feedstock/tree/fremor0.9.3
- [ ] adjust the version to `X.Y.Z` and update the `sha256` to what it says on PyPI in `recipe.yaml`
- [ ] open a PR to the `conda-forge/fremor-feedstock` e.g. https://github.com/conda-forge/fremor-feedstock/pull/3
- [ ] once checks pass, a reviewer with access to `conda-forge/fremor-feedstock` can approve and merge, kicking off the rest of the publishing pipeline to `conda-forge`


### wrap-up

- [ ] back to the `fremor` PR we opened intially.
- [ ] edit the version number in `fremor/_version.py` to `X.Y.Z.post`, let the checks pass
- [ ] merge the PR branch you used for creating the release to `main`
