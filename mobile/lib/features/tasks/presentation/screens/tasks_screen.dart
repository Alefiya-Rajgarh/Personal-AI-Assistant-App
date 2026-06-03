import 'package:flutter/material.dart';

import '../../../../core/widgets/aegis_empty_state.dart';

class TasksScreen extends StatelessWidget {
  const TasksScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Tasks')),
      body: const AegisEmptyState(
        icon: Icons.check_circle_outline,
        title: 'No tasks yet',
        subtitle: 'Create tasks to keep your day on track.',
      ),
    );
  }
}
