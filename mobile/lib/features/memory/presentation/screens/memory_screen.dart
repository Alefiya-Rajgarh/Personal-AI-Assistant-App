import 'package:flutter/material.dart';

import '../../../../core/widgets/aegis_empty_state.dart';

class MemoryScreen extends StatelessWidget {
  const MemoryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Memory vault')),
      body: const AegisEmptyState(
        icon: Icons.bookmark_border,
        title: 'Nothing stored yet',
        subtitle: 'Save decisions, preferences, and meeting notes here.',
      ),
    );
  }
}
