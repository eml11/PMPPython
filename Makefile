ROOTDIR="."
SAMPLES=${ROOTDIR}/samples
DATA=${ROOTDIR}/data
TEX=${ROOTDIR}/tex

DOCBASE="python_course"

doc:
	cd ${TEX} && latex ${DOCBASE}.tex
	cd ${TEX} && latex ${DOCBASE}.tex
	cp ${TEX}/${DOCBASE}.pdf .
