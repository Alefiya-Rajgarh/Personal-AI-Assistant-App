import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../../../../core/widgets/aegis_card.dart';
import '../../../../core/theme/aegis_spacing.dart';

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Settings')),
      body: ListView(
        padding: const EdgeInsets.all(AssistanceSpacing.lg),
        children: [
          AegisCard(
            onTap: () => context.go('/settings/preferences'),
            child: const Text('Preferences'),
          ),
          const SizedBox(height: AssistanceSpacing.md),
          AegisCard(
            onTap: () => context.go('/settings/integrations'),
            child: const Text('Integrations'),
          ),
        ],
      ),
    );
  }
}
