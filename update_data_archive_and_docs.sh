pushd corecon/data
python make_data_archive.py
popd

pushd docs/
source prepare_build_docs.sh
popd

