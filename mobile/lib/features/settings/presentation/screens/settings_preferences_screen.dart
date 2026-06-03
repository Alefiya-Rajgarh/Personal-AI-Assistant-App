import 'package:flutter/material.dart';

import '../../../../core/widgets/aegis_empty_state.dart';

class SettingsPreferencesScreen extends StatelessWidget {
  const SettingsPreferencesScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Preferences')),
      body: const AegisEmptyState(
        icon: Icons.tune,
        title: 'No preferences yet',
        subtitle: 'Personalize your assistant and notification styles.',
      ),
    );
  }
}
