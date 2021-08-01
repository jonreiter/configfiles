function cl() {
	DIR="$*";
	if [ $# -lt 1 ]; then
		DIR=${HOME};
	fi;
	builtin cd "${DIR}" && \
		ls -F --color=auto
}
