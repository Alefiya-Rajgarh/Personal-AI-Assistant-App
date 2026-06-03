import 'package:flutter/material.dart';

import '../../../../core/theme/aegis_spacing.dart';
import '../../../../core/widgets/aegis_card.dart';

class TaskDetailScreen extends StatelessWidget {
  const TaskDetailScreen({super.key, required this.taskId});

  final String taskId;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Task $taskId')),
      body: Padding(
        padding: const EdgeInsets.all(AssistanceSpacing.lg),
        child: const AegisCard(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('Draft board update'),
              SizedBox(height: AssistanceSpacing.sm),
              Text('Due today • Priority high'),
            ],
          ),
        ),
      ),
    );
  }
}
