cmake_minimum_required(VERSION 2.8)
project(ecto_talk)
find_package(ecto REQUIRED)

set(outdir ${CMAKE_BINARY_DIR}/doc/talk)

file(MAKE_DIRECTORY ${outdir})

foreach(VER notes overhead)
  add_custom_command(OUTPUT ${outdir}/${VER}.pdf
    COMMAND pdflatex
    -output-directory=${outdir} -file-line-error -halt-on-error
    ${CMAKE_CURRENT_SOURCE_DIR}/${VER}.tex
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    DEPENDS
    ${CMAKE_CURRENT_SOURCE_DIR}/main.tex
    ${CMAKE_CURRENT_SOURCE_DIR}/${VER}.tex
    ${CMAKE_CURRENT_SOURCE_DIR}/beamerthemeresophonic.sty
    )
endforeach()

add_custom_target(talk-pdf
  DEPENDS
  ${outdir}/overhead.pdf
  ${outdir}/notes.pdf
  )
