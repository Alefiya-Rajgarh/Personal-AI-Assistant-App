import 'package:flutter/material.dart';

import '../../../../core/widgets/aegis_empty_state.dart';

class SettingsIntegrationsScreen extends StatelessWidget {
  const SettingsIntegrationsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Integrations')),
      body: const AegisEmptyState(
        icon: Icons.extension_outlined,
        title: 'No integrations connected',
        subtitle: 'Connect calendar, email, and CRM accounts here.',
      ),
    );
  }
}
