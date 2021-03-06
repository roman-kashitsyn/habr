{
  'includes': ['../conf.gypi'],
  'targets': [
    {
      'target_name': 'miniregex',
      'type': 'static_library',
      'defines': [],
      'include_dirs': ['include'],
      'sources': [
        'include/miniregex.hpp',
        'src/miniregex.cpp',
      ],
      'direct_dependent_settings': {
        'include_dirs': ['include'],
      },
    },
    {
      'target_name': 'miniregex_test',
      'type': 'executable',
      'dependencies': ['../gtest-1.6/gtest.gyp:gtest',
                       '../gtest-1.6/gtest.gyp:gtest_main',
                       'miniregex',],
      'sources': [
        'src/test/test_miniregex.cpp',
      ],
    },
  ],

}
