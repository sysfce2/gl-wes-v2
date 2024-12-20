#! /usr/bin/env python
# encoding: utf-8
# mittorn, 2018

from waflib import Logs
import os

top = '.'

def options(opt):
	# stub
	return

def configure(conf):
	if conf.env.DEST_OS2 == 'android':
		conf.check_cc(lib='log')
	conf.define('WES_MANGLE_PREPEND', 1)

	# Xash3D doesn't use GLU
	# conf.define('WES_ENABLE_GLU', 1)

	conf.define('REF_DLL', 1)
	return

def build(bld):
	source = bld.path.ant_glob(['src/*.c'])
	libs = ['werror']
	if bld.env.DEST_OS2 == 'android':
		libs += ['LOG']
	includes = ['src/']

	bld.stlib(
		source   = source,
		target   = 'gl-wes-v2',
		includes = includes,
		use      = libs
	)
