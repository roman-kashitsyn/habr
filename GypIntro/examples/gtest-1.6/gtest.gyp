{
  'includes': ['../conf.gypi'],
  'targets': [                     # <- Список целей
    # Первая цель
    {
      'target_name': 'gtest',      # <- Имя цели
      'cflags': ['-pthread'],      # <- Флаги компиляции
      'link_settings': {           # <- Настройки линковщика
        'libraries': ['-lpthread'] # <- Список необходимых библиотек
      },
      'type': 'static_library',    # <- Тип цели, возможны варианты static_library,
                                   # shared_library, executable, none

      'standalone_static_library': 1, # <- Не собирать библиотеку как thin archive
                                      # Опция может быть недоступна в старых версиях GYP

      'sources': [                 # <- Список исходных файлов
        'include/gtest/gtest-death-test.h',
        'include/gtest/gtest-message.h',
        'include/gtest/gtest-param-test.h',
        'include/gtest/gtest-printers.h',
        'include/gtest/gtest-spi.h',
        'include/gtest/gtest-test-part.h',
        'include/gtest/gtest-typed-test.h',
        'include/gtest/gtest.h',
        'include/gtest/gtest_pred_impl.h',
        'include/gtest/internal/gtest-death-test-internal.h',
        'include/gtest/internal/gtest-filepath.h',
        'include/gtest/internal/gtest-internal.h',
        'include/gtest/internal/gtest-linked_ptr.h',
        'include/gtest/internal/gtest-param-util-generated.h',
        'include/gtest/internal/gtest-param-util.h',
        'include/gtest/internal/gtest-port.h',
        'include/gtest/internal/gtest-string.h',
        'include/gtest/internal/gtest-tuple.h',
        'include/gtest/internal/gtest-type-util.h',
        'src/gtest-all.cc',
        'src/gtest-death-test.cc',
        'src/gtest-filepath.cc',
        'src/gtest-internal-inl.h',
        'src/gtest-port.cc',
        'src/gtest-printers.cc',
        'src/gtest-test-part.cc',
        'src/gtest-typed-test.cc',
        'src/gtest.cc',
      ],
      'sources!': [                      # <- Эти исходные файлы нужно исключить,
        'src/gtest-all.cc',              # эту директиву удобно использовать в
      ],                                 # секциях conditions

      'include_dirs': [                  # <- Список каталогов с заголовочными файлами
        '.',
        './include',
      ],
      'conditions': [                    # <- Раздел с конфигурацией, зависящей от
        ['OS == "linux"', {              # платформы и целевого формата
          'defines': [
            'GTEST_HAS_RTTI=0',
          ],
          'direct_dependent_settings': {
            'defines': [
              'GTEST_HAS_RTTI=0',
            ],
          },
        }],
        ['OS=="win" and (MSVS_VERSION=="2012" or MSVS_VERSION=="2012e")', {
          'defines': [
            '_VARIADIC_MAX=10',
          ],
          'direct_dependent_settings': {
            'defines': [
              '_VARIADIC_MAX=10',
            ],
          },
        }],
      ],
      'direct_dependent_settings': { # <- Настройки, которые будут добавлены к целям,
                                     # использующим цель gtest прямую, т.е. не транзитивно

        'defines': [                 # <- Определения препроцессора
          'UNIT_TEST',
        ],
        'include_dirs': [            # <- Каталог с заголовочными файлами include будет
          'include',                 # автоматически добавлен всем зависимым целям,
        ],                           # причём будет использован абсолютный путь, рассчитанный
                                     # как </path/to/this/gypfile>/include

        'msvs_disabled_warnings': [4800],
      },
    },
    # Вторая цель
    {
      'target_name': 'gtest_main',
      'type': 'static_library',
      'standalone_static_library': 1,
      'dependencies': ['gtest'],     # <- Список зависимостей цели, в данном случае
                                     # вторая цель зависит от первой
      'sources': [
        'src/gtest_main.cc',
      ],
    },
  ],
}
