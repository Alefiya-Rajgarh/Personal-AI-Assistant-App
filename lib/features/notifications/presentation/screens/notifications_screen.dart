import 'package:flutter/material.dart';

import '../../../../core/widgets/aegis_empty_state.dart';

class NotificationsScreen extends StatelessWidget {
  const NotificationsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Notifications')),
      body: const AegisEmptyState(
        icon: Icons.notifications_outlined,
        title: 'All clear',
        subtitle: 'You are caught up on alerts and updates.',
      ),
    );
  }
}
