{
  'target_defaults': {
    'configurations': {
      'Release': {
        'conditions': [
          ['OS=="linux"', {
              'cflags': ['-O2']
            }]
        ]
      },
      'Debug': {
        'conditions': [
          ['OS=="linux"', {
              'cflags': ['-g']
            }]
        ]
      },
    },
  },
}
